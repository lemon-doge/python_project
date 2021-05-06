matrix = []
for i in range(11):
    matrix.append(list(map(int, input().strip().split('\t'))))
    k = 1
    for j in range(len(matrix[i])):
        matrix[i][j] *= k
        k*= -1
print(matrix)

print('\n')

linearKef = []
for i in range(9,-1,-1):
    k = matrix[10][10-i]
    linearKef.append(k)
    for j in range(len(matrix[i])):
        matrix[10][j+10-i] -= matrix[i][j] * k
    print(matrix[10])

print('\n')

linearKef.reverse()
print(linearKef)

# [[1],
# [1, -1],
# [1, -2, 1],
# [1, -3, 3, -1],
# [1, -4, 6, -4, 1],
# [1, -5, 10, -10, 5, -1],
# [1, -6, 15, -20, 15, -6, 1],
# [1, -7, 21, -35, 35, -21, 7, -1],
# [1, -8, 28, -56, 70, -56, 28, -8, 1],
# [1, -9, 36, -84, 126, -126, 84, -36, 9, -1],
# [1, -10, 45, -120, 210, -252, 210, -120, 45, -10, 1]]

# [-1, 10, -45, 120, -210, 252, -210, 120, -45, 10]