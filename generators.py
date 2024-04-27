from random_solution import random_solution
import random
from copy import deepcopy

NB_SIZE = 50


def full_random(G, routes: list):
    result = []

    for _ in range(10):
        result.append(random_solution(G))
    return result

def half_random(G, routes_src: list):
    result = []
    for i in range(NB_SIZE):
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

#Generator rozwiązań przyjmuje graf i obecny podział tras jako listę (przykład: [[1, 2, 3]. [4, 5, 6]. [7]]). Powinien zwracać listę, która zawiera rozwiązania podobne do przekazanego jako .