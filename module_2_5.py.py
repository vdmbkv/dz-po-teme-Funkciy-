# Матрица воплоти

def get_matrix(n, m, value):
    matrix = []
    for lin in range(n):
        matrix.append([])
        for colum in range(m):
            matrix[lin].append(value)

    return matrix

result1, result2, result3 = get_matrix(2, 2, 3), get_matrix(3, 5, 42), get_matrix(4, 2, 13)
print(result1, result2, result3, sep='\n')
