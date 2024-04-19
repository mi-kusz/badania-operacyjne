from random_solution import example_graph
from bees_algorithm import bees_algorithm
import generators


def main():
    G = example_graph()

    cost, driver_routes = bees_algorithm(G, 15, 2, 2, generators.full_random, generators.full_random, 1, 1, 20)

    print(f"Koszt rozwiązania: {cost}")
    
    for index, routes in enumerate(driver_routes):
        print(f"Kierowca {index}: {routes}")


if __name__ == "__main__":
    main()