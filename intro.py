import numpy as n
matrix = n.eye(3)
print(matrix)
matrix[matrix != 1] += 3
print(matrix)
matrix[matrix != 1] += 3
matrix = n.delete(matrix, -1, 1)
print(matrix)