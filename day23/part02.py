from pathlib import Path
from collections import deque

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


def bfs(graph: dict[str, set[str]], v: str) -> set[str]:
    visited: set[str] = set()
    q: deque[str] = deque()
    q.append(v)
    while len(q) != 0:
        u = q.popleft()
        if u in visited:
            continue
        for n in graph[u]:
            if n in visited or n in q:
                continue
            q.append(n)
        visited.add(u)
    return visited


for v in connections:
    to_remove: set[str] = set()
    for n1 in connections[v]:
        cycle_found = False
        for n2 in connections[n1]:
            if n2 == v:
                continue
            if v in connections[n2]:
                cycle_found = True
        if not cycle_found:
            to_remove.add(n1)
    connections[v].difference_update(to_remove)
    for u in to_remove:
        connections[u].discard(v)

cliques: list[set[str]] = []
visited: set[str] = set()
for v in connections:
    if v in visited:
        continue
    cliques.append(bfs(connections, v))
    visited = visited.union(cliques[-1])


def is_fully_connected(clique: set[str]) -> bool:
    for v in clique:
        if len(connections[v]) != len(clique) - 1:
            return False
    return True


computers = [i for i in filter(is_fully_connected, cliques)]
print(",".join(sorted(computers[0])))
