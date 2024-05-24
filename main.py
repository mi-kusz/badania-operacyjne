from bees_algorithm import bees_algorithm
from draw_solution import draw_solution
import generators
import pickle


def main():
    #Parametry (można dodać wczytywanie jako parametry programu)
    scouts = 15
    elite_places = 2
    good_places = 2
    elite_generator = generators.full_random
    good_generator = generators.full_random
    bees_per_elite_place = 2
    bees_per_good_place = 2
    iterations = 20
    drivers = 3

    graph_path = 'graphs/small_graph.data'
    with open(graph_path, 'rb') as f:
        G = pickle.load(f)

    cost, driver_routes, costs_per_iteration = bees_algorithm(G,
                                         scouts,
                                         elite_places, 
                                         good_places,
                                         elite_generator,
                                         good_generator,
                                         bees_per_elite_place,
                                         bees_per_good_place,
                                         iterations,
                                         drivers)

    print(f"Koszt rozwiązania: {cost}")

    for index, routes in enumerate(driver_routes):
        print(f"Kierowca {index}: {routes}")

    print("Wartości funkcji celu w kolejnych iteracjach:", costs_per_iteration)

    draw_solution(G, driver_routes)


if __name__ == "__main__":
    main()