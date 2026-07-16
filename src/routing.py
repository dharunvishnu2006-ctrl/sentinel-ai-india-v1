from collections import deque

def shortest_path(graph: dict, start: str, goal: str) -> list:
    """BFS: return the shortest list of agents start->goal."""
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return []