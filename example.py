import random


def example_graph() -> list:
    return [
        [(2, 0.26), (4, 0.38), (6, 0.58), (7, 0.16)],
        [(2, 0.36), (3, 0.29), (5, 0.32), (7, 0.19)],
        [(0, 0.26), (1, 0.36), (3, 0.17), (6, 0.40), (7, 0.34)],
        [(1, 0.29), (2, 0.17), (6, 0.52)],
        [(0, 0.38), (5, 0.35), (6, 0.93), (7, 0.37)],
        [(1, 0.32), (4, 0.35), (7, 0.28)],
        [(0, 0.58), (2, 0.40), (3, 0.52), (4, 0.93)],
        [(0, 0.16), (1, 0.19), (2, 0.34), (4, 0.37), (5, 0.28)]
    ]


def random_solution(G: list) -> list:
    permutation = list(range(1, len(G)))
    random.shuffle(permutation)

    result = []

    current_index = 0

    while current_index < len(permutation):
        cycle_length = random.randint(1, 3)

        result.append(permutation[current_index: current_index + cycle_length])

        current_index += cycle_length
    
    return result