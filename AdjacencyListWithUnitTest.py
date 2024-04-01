def mat_to_list(adj_mat):
    result = []
    for i in range(len(adj_mat)):
        list = []
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 1:
                list.append(j)
        result.append(list)
    return result

def test_mat_to_list():
    adjacency_matrix = [
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    assert mat_to_list(adjacency_matrix) == [[1, 3], [2], [0], [4], [3], []]
    adjacency_matrix1 = [
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 0]
    ]
    assert mat_to_list(adjacency_matrix1) == [[1, 2], [0], [0]]
    adjacency_matrix2 = [
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    assert mat_to_list(adjacency_matrix2) == [[1, 3], [0, 2]]
    adjacency_matrix3 = []
    assert mat_to_list(adjacency_matrix3) == []
    adjacency_matrix4 = [[0]]
    assert mat_to_list(adjacency_matrix4) == [[]]
    print("All tests passed!")
test_mat_to_list()
