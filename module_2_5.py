def get_matrix(n, m, value):
    matrix = []

    for i in range(m):
        for j in range(n):
            matrix.append([value]*m)
        return print(matrix)


result_1 = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 13)

