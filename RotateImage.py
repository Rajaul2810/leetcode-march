def RotateImage(matrix):
    # n = len(matrix)
    # for i in range(n):
    #     for j in range(i):
    #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix[:] = zip(*matrix[::-1])
    return matrix
print(RotateImage([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))