from utils import get_solution_cost, floyd_warshall
from random_solution import random_solution
import random


def bees_algorithm(G: list,
                   initial_scouts: int,
                   elite_places_number: int,
                   good_places_number: int,
                   elite_neighborhood_generator,
                   good_neighborhood_generator,
                   elite_place_bees_number: int,
                   good_place_bees_number: int,
                   iterations: int
                   ) -> tuple:
    
    #Oblicz odległości każdy z każdym
    D = floyd_warshall(G)

    #Jeszcze nie znaleziono najlepszego rozwiązania
    best_solution = None
    best_cost = float('inf')
    
    #Wygeneruj tyle losowych rozwiązań ile jest pszczół zwiadowców i posortuj je od najlepszego do najgorszego
    places = [random_solution(G) for _ in range(initial_scouts)]
    places = sorted([(get_solution_cost(D, x), x) for x in places])
    #Pierwsze elite_places_number miejsca to miejsca elitarne, kolejne good_places_number to miejsca dobre (pozostałe są ignorowane)

    for _ in range(iterations):
        #Jeśli najlepsze rozwiązanie w danej iteracji jest lepsze od dotychczas najlepszego to je zapisz
        if places[0][0] < best_cost:
            best_solution = places[0][1].copy()
            best_cost = places[0][0]

        new_places = []

        #Powtórz dla wszystkich miejsc elitarnych
        for elite_place in places[:elite_places_number]:
            #Wybierz elite_place_bees_number losowych rozwiązań z sąsiedztwa miejsca elitarnego
            neighborhood = random.sample(elite_neighborhood_generator(G, elite_place), elite_place_bees_number)

            #Najlepsze znalezione rozwiązanie z sąsiedztwa dodaj do miejsc kolejnej iteracji
            best = sorted([(get_solution_cost(D, x), x) for x in neighborhood])[0]
            new_places.append(best)
        
        #Powtórz dla wszystkich dobrych miejsc
        for good_place in places[elite_places_number: elite_places_number + good_places_number]:
            #Wybierz good_place_bees_number losowych rozwiązań z sąsiedztwa dobrego miejsca
            neighborhood = random.sample(good_neighborhood_generator(G, good_place), good_place_bees_number)

            #Najlepsze znalezione rozwiązanie z sąsiedztwa dodaj do miejsc kolejnej iteracji
            best = sorted([(get_solution_cost(D, x), x) for x in neighborhood])[0]
            new_places.append(best)
        
        #Pozostałe pszczoły szukają rozwiązania losowo
        for _ in range(len(places) - (elite_places_number + good_places_number)):
            x = random_solution(G)
            new_places.append((get_solution_cost(D, x), x))
        
        #Posortuj rozwiązania do kolejnej iteracji
        places = sorted(new_places)

    return get_solution_cost(D, best_solution, return_best_assignment=True)
