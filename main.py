from bees_algorithm import bees_algorithm
from draw_solution import draw_solution
import pickle
import utils


def main():
    #Parametry (można dodać wczytywanie jako parametry programu)
    args = utils.setup_parser().parse_args()
    scouts = args.scouts
    elite_places = args.elite_places
    good_places = args.good_places
    elite_generator = utils.generators_map[args.elite_generator]
    good_generator = utils.generators_map[args.good_generator]
    bees_per_elite_place = args.bees_per_elite_place
    bees_per_good_place = args.bees_per_good_place
    iterations = args.iterations
    drivers = args.drivers

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