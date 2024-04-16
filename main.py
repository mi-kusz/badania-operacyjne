from utils import get_solution_cost
from example import example_graph, random_solution
from brute_force import brute_force


def main():
    G = example_graph()

    #possible_solution = random_solution(G)
    #print(f"Trasy: {possible_solution}")

    #max_cost, driver_routes = get_solution_cost(G, possible_solution)
    max_cost, driver_routes = brute_force(G)

    print(f"Koszt rozwiązania: {max_cost}")
    
    for index, routes in enumerate(driver_routes):
        print(f"Kierowca {index}: {routes}")


if __name__ == "__main__":
    main()