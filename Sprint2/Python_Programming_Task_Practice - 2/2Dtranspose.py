matrix=[[1,2,3],[4,5,6],[7,8,9]]
newmatrix=[[0 for _ in range (len(matrix))] for _ in range (len(matrix[0]))]
for i in range (0,len(matrix)):
    for j in range(0,len(matrix[i])):
        newmatrix[i][j]=matrix[j][i]

print(newmatrix)