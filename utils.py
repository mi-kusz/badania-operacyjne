from queue import PriorityQueue
from collections import deque
import argparse
import generators


generators_map = {1: generators.full_random, 2: generators.half_random, 3: generators.enlarge_routes}

def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scouts', type=int, help='Number of scouts', default=15)
    parser.add_argument('--elite_places', type=int, help='Number of elite places', default=2)
    parser.add_argument('--good_places', type=int, help='Number of good places', default=2)
    parser.add_argument('--elite_generator', type=int, help='Elite generator: 1 - full random, 2 - half random, 3 - enlarge routes', default=1)
    parser.add_argument('--good_generator', type=int, help='Good generator: 1 - full random, 2 - half random, 3 - enlarge routes', default=1)
    parser.add_argument('--bees_per_elite_place', type=int, help='Number of bees per elite place', default=2)
    parser.add_argument('--bees_per_good_place', type=int, help='Number of bees per good place', default=2)
    parser.add_argument('--iterations', type=int, help='Number of iterations', default=20)
    parser.add_argument('--drivers', type=int, help='Number of drivers', default=3)
    return parser


# Baza zawsze ma index 0, reszta to miasta


def floyd_warshall(G: list) -> list:
    n = len(G)
    D = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        D[i][i] = 0
    
    for index, neighbors in enumerate(G):
        for neighbor, weight in neighbors:
            D[index][neighbor] = weight
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    
    return D


def floyd_warshall_paths(G: list) -> list:
    n = len(G)
    D = [[float('inf') for _ in range(n)] for _ in range(n)]
    next = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        D[i][i] = 0
        next[i][i] = -1
    
    for index, neighbors in enumerate(G):
        for neighbor, weight in neighbors:
            D[index][neighbor] = weight
            next[index][neighbor] = neighbor
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    next[i][j] = k
    
    return next


def calculate_route_cost(route: list, D: list) -> float:
    cost = 0

    #Koszt przejazdu między miastami
    for i in range(len(route) - 1):
        cost += D[route[i]][route[i + 1]]
    
    #Dojechanie od bazy do pierwszego miasta
    cost += D[0][route[0]]

    #Dojechanie od ostatniego miasta do bazy
    cost += D[route[-1]][0]

    return cost


def get_solution_cost(D: list, routes: list, drivers_number: int, return_best_assignment: bool = False):
    #Posortowanie po długości trasy
    routes_with_costs = deque(sorted([(calculate_route_cost(x, D), x) for x in routes], reverse=True))

    routes_drivers_assignment = [[] for _ in range(drivers_number)]
    final_cost = 0
    pq = PriorityQueue()

    for i in range(drivers_number):
        pq.put((0, i))
    
    #Wyciąganie z kolejki priorytetowej kierowcy, który naszybciej będzie dostępny i przypisanie mu zadania
    while len(routes_with_costs) > 0:
        current_cost, route = routes_with_costs.popleft()
        cumulated_cost, driver = pq.get()
        routes_drivers_assignment[driver].append(route)

        new_cost = cumulated_cost + current_cost

        pq.put((new_cost, driver))
        final_cost = max(final_cost, new_cost)
    
    if return_best_assignment:
        return final_cost, routes_drivers_assignment
    else:
        return final_cost
