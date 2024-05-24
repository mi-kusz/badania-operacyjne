from random_solution import random_solution
import random
from copy import deepcopy

NB_SIZE = 50


def full_random(G: list, routes: list, solutions_to_generate: int) -> list:
    result = []

    for _ in range(solutions_to_generate):
        result.append(random_solution(G))
    return result


def half_random(G, routes_src: list, solutions_to_generate: int):
    result = []
    for i in range(solutions_to_generate):
        routes = deepcopy(routes_src[1])
        random_pair = random.sample([i for i in range(len(routes))], 2)
        route_A_idx = random_pair[0]
        route_B_idx = random_pair[1]
        decisions = []
        if len(routes[route_A_idx]) > 0 and len(routes[route_B_idx]) > 0: decisions.append("swap")
        if len(routes[route_A_idx]) < 3 and len(routes[route_B_idx]) > 0: decisions.append("receive")
        if len(routes[route_B_idx]) < 3 and len(routes[route_A_idx]) > 0: decisions.append("give")
        if len(decisions) == 0: continue
        decision = random.choice(decisions)
        if decision == "give":
            city_A = random.choice(routes[route_A_idx])
            routes[route_B_idx].append(city_A)
            routes[route_A_idx].remove(city_A)
            if (len(routes[route_A_idx]) == 0): 
                routes.pop(route_A_idx)
        elif decision == "receive":
            city_B = random.choice(routes[route_B_idx])
            routes[route_A_idx].append(city_B)
            routes[route_B_idx].remove(city_B)
            if (len(routes[route_B_idx]) == 0): 
                routes.pop(route_B_idx)
        elif decision == "swap":
            city_A = random.choice(routes[route_A_idx])
            city_B = random.choice(routes[route_B_idx])
            routes[route_B_idx].append(city_A)
            routes[route_A_idx].remove(city_A)
            routes[route_A_idx].append(city_B)
            routes[route_B_idx].remove(city_B)
        result.append(routes)
    return result


#Generator łączy trasy o długości 1 z trasami o długości 2, żeby jak najwięcej tras miało długość 3
def enlarge_routes(G: list, routes: list, solutions_to_generate: int) -> list:
    routes = deepcopy(routes[1])
    result = []

    for _ in range(solutions_to_generate):
        short_routes = []
        medium_routes = []
        long_routes = []

        #Podziel trasy ze względu na długość
        for route in routes:
            match len(route):
                case 1:
                    short_routes.append(route)
                case 2:
                    medium_routes.append(route)
                case 3:
                    long_routes.append(route)
        
        #Dopóki są krótkie trasy
        while len(short_routes) > 0 and len(medium_routes) > 0:
            give = random.choice(short_routes)
            short_routes.remove(give)

            take = random.choice(medium_routes)
            medium_routes.remove(take)

            index = random.randint(0, 2)
            long_routes.append(take[:index] + give + take[index:])
        
        result.append(short_routes + medium_routes + long_routes)

    return result


#Generator rozwiązań przyjmuje graf i obecny podział tras jako listę (przykład: [[1, 2, 3]. [4, 5, 6]. [7]]). Powinien zwracać listę, która zawiera rozwiązania podobne do przekazanego jako parametr.