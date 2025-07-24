#Example 2:Rotate Matrix by 90 degree leetCode 48
#Brute Solution
Matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
def Rotate(Matrix):
    n=len(Matrix)
    Result=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            Result[j][(n-1)-i]=Matrix[i][j]
    print(Result)
Rotate(Matrix)
#Optimal Solution
def RotateMatrix(Matrix):
    n=len(Matrix)
    for i in range(0,n-1):
        for j in range(i+1,n):
            #Taking transpose
            Matrix[i][j],Matrix[j][i]=Matrix[j][i],Matrix[i][j]
    for i in range(0,n):
        Matrix[i].reverse()
    return Matrix
print(RotateMatrix(Matrix))
       