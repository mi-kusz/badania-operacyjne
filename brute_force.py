import itertools
from utils import get_solution_cost


def generate_all_possibilites(n: int, max_cycle_length: int = 3):
    def recurrence(permutation: tuple, current_index: int, result: list):
        if current_index == len(permutation):
            yield result
        else:
            for length in range(1, min(max_cycle_length, len(permutation) - current_index) + 1):
                result.append(permutation[current_index: current_index + length])
                yield from recurrence(permutation, current_index + length, result)
                result.pop()

    for permutation in itertools.permutations(range(1, n)):
        yield from recurrence(permutation, 0, [])


def brute_force(G: list) -> tuple:
    best_solution_cost = float('inf')
    best_solution_assignments = None

    for routes in generate_all_possibilites(len(G)):
        cost, assignments = get_solution_cost(G, routes)

        if cost < best_solution_cost:
            best_solution_cost = cost
            best_solution_assignments = assignments
    
    return best_solution_cost, best_solution_assignments