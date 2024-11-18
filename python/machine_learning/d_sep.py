
from collections import deque


def build_graph(movies):
    graph = {}
    for movie, actors in movies.items():
        for actor in actors:
            if actor not in graph:
                graph[actor] = set()
            for co_actor in actors:
                if actor != co_actor:
                    graph[actor].add(co_actor)
    return graph


def find_degrees_of_separation(graph, start_actor, target_actor):
    if start_actor == target_actor:
        return 0
    visited = set()
    queue = deque([(start_actor, 0)])
    while queue:
        current_actor, degrees = queue.popleft()
        if current_actor == target_actor:
            return degrees
        if current_actor not in visited:
            visited.add(current_actor)
            for neighbor in graph[current_actor]:
                if neighbor not in visited:
                    queue.append((neighbor, degrees + 1))
    return -1


movies = {
    'Movie 1': {'Actor A', 'Actor B', 'Actor C'},
    'Movie 2': {'Actor B', 'Actor D', 'Actor E'},
    'Movie 3': {'Actor C', 'Actor E'},
    'Movie 4': {'Actor D', 'Actor F'},
    'Movie 5': {'Actor A', 'Actor F'}
}
graph = build_graph(movies)
start = 'Actor A'
target = 'Actor E'
degrees = find_degrees_of_separation(graph, start, target)
if degrees == -1:
    print(f"There is no connection between {start} and {target}.")
else:
    print(f"The degree of separation between {
          start} and {target} is {degrees}.")
