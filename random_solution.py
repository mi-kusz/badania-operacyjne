import random


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
