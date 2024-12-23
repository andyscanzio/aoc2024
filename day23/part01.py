from pathlib import Path

folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

links = [line.split("-") for line in data.splitlines()]

connections: dict[str, set[str]] = {}

for a, b in links:
    if a in connections:
        connections[a].add(b)
    else:
        connections[a] = {b}
    if b in connections:
        connections[b].add(a)
    else:
        connections[b] = {a}


def find_cycles_of_length_k(
    graph: dict[str, set[str]], k: int
) -> list[tuple[str, ...]]:
    def dfs(start: str, current: str, visited: set[str], path: list[str]):
        if len(path) == k:
            # Check if the current path forms a cycle
            if start in graph[current]:
                cycle = tuple(sorted(path))
                cycles.add(cycle)
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(start, neighbor, visited, path + [neighbor])
                visited.remove(neighbor)

    cycles: set[tuple[str, ...]] = set()
    for node in graph:
        visited = {node}
        dfs(node, node, visited, [node])

    return [cycle for cycle in cycles]


triangles = find_cycles_of_length_k(connections, 3)

print(sum(map(lambda x: any(i[0] == "t" for i in x), triangles)))
