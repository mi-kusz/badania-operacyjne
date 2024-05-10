import matplotlib.pyplot as plt
import networkx as nx
from utils import floyd_warshall_paths


def get_edges_between_vertices(u: int, v: int, next: list) -> set:
    result = set()

    #Trasa z u do v. Dopóki nie dojdziesz do docelowego, zbliżaj się o jeden krok do celu
    while next[u][v] != -1:
        result.add((u, next[u][v]))
        u = next[u][v]
    
    return result


def get_edges_to_color(route: list, next: list) -> set:
    result = set()
    
    #Krawędzie pomiędzy wierzchołkami w których zostawiamy towar na trasie
    for i in range(len(route) - 1):
        result |= get_edges_between_vertices(route[i], route[i + 1], next)
    
    #Krawiędzie pomiędzy bazą i pierwszym wierzchołkiem, w którym zostawiamy towar
    result |= get_edges_between_vertices(0, route[0], next)

    #Krawędzie pomiędzy ostatnim wierzchołkiem, w którym zostawiamy towar, a bazą
    result |= get_edges_between_vertices(route[-1], 0, next)

    return result
    

def draw_solution(G: list, drivers_routes: list) -> None:
    #Utwórz graf biblioteki networkx
    graph = nx.Graph()
    next = floyd_warshall_paths(G)

    for i in range(len(G)):
        for neighbor, weight in G[i]:
            if neighbor > i:
                graph.add_edge(i, neighbor, weight=weight)
    
    #Używane, żeby wierzchołki na każdym obrazie były w tym samym miejscu
    pos = nx.circular_layout(graph)

    for driver_index, driver_routes in enumerate(drivers_routes):
        n = len(driver_routes)

        #Osobne okno dla każdego kierowcy
        plt.figure()
        plt.title(f'Trasy kierowcy numer {driver_index}')
        plt.xticks([])
        plt.yticks([])

        for route_index, single_route in enumerate(driver_routes):
            edges_to_color = get_edges_to_color(single_route, next)
            colors = [('r' if (u, v) in edges_to_color or (v, u) in edges_to_color else 'b') for u, v in graph.edges()]

            if n == 1:
                plt.subplot(1, 1, 1)
            else:
                plt.subplot((n // 2) if (n % 2 == 0) else (n // 2 + 1), 2, route_index + 1)
            nx.draw(graph, pos, edge_color=colors, with_labels=True)
        
    plt.show()