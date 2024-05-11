from random_solution import example_graph
from bees_algorithm import bees_algorithm
import generators
from draw_solution import draw_solution


def main():
    G = example_graph()

    cost, driver_routes = bees_algorithm(G, 15, 2, 2, generators.enlarge_routes, generators.enlarge_routes, 1, 1, 20)

    print(f"Koszt rozwiązania: {cost}")
    
    for index, routes in enumerate(driver_routes):
        print(f"Kierowca {index}: {routes}")
    
    draw_solution(G, driver_routes)


if __name__ == "__main__":
    main()