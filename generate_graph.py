import random
import pickle

def generate_complete_graph(n: int) -> None:
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            weight = random.randint(1, 50)

            graph[i].append((j, weight))
            graph[j].append((i, weight))

    with open(f'graphs/complete{n}.data', 'wb') as f:
        pickle.dump(graph, f)
