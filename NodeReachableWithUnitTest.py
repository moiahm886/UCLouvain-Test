def reachable(adj_list, start_node):
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            neighbors = adj_list[node]
            for neigh in neighbors:
                if neigh not in visited:
                    stack.append(neigh)
    return visited
def test_reachable():
    adjacency_list = [[1, 3], [2], [0], [4], [3], []]
    assert reachable(adjacency_list, 0) == {0, 1, 2, 3, 4}
    assert reachable(adjacency_list, 2) == {0, 1, 2, 3, 4}
    assert reachable(adjacency_list, 4) == {3, 4}
    assert reachable(adjacency_list, 5) == {5}
    print("All tests passed!")
test_reachable()

