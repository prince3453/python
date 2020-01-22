mat1=[[2,3,5],[5,4,2],[9,7,5]]
mat2=[[9,8,7],[8,4,2],[1,2,3]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        for k in range(len(mat2)):
            result[i][j] += mat1[i][k]*mat2[k][j]
for i in  result:
    print(i)
