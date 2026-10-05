import subprocess
subprocess.run('cls', shell=True)

def rotateImage(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for rev in matrix:
        rev.reverse()

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotateImage(matrix))






















