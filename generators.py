from random_solution import random_solution


def full_random(G, routes: list):
    result = []

    for _ in range(10):
        result.append(random_solution(G))
    
    return result

#Generator rozwiązań przyjmuje graf i obecny podział tras jako listę (przykład: [[1, 2, 3]. [4, 5, 6]. [7]]). Powinien zwracać listę, która zawiera rozwiązania podobne do przekazanego jako .