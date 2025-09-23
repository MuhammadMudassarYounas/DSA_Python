#Example 9 : Rat in Maze //GFG

def RatMaze(matrix):
    n=len(matrix)
    ans=[]
    vis=[[0 for _ in range(n)] for _ in range(n)]
    if matrix[0][0]==1:
        return findPathHelper(0,0,matrix,n,ans,"",vis)
    return ans
def findPathHelper(i,j,a,n,ans,move,vis):
    if i==n-1 and j==n-1:
        ans.append(move)
        return
    #downWard
    if i+1<n and not vis[i+1][j] and a[i+1][j]==1:
        vis[i][j]=1
        findPathHelper(i+1,j,a,n,ans,move+"D",vis)
        vis[i][j]=0

    #left
    if j+1>=0 and not vis[i][j-1] and a[i][j-1]==1:
        vis[i][j]=1
        findPathHelper(i,j-1,a,n,ans,move+"L",vis)
        vis[i][j]=0

    #Right
    if j+1<n and not vis[i][j+1] and a[i][j+1]==1:
        vis[i][j]=1
        findPathHelper(i,j+1,a,n,ans,move+"R",vis)
        vis[i][j]=0

    #Upward
    if i-1>=0 and not vis[i-1][j] and a[i-1][j]==1:
        vis[i][j]=1
        findPathHelper(i-1,j,a,n,ans,move+"U",vis)
        vis[i][j]=0

matrix=[[1,0,0,0],
        [1,1,0,0],
        [1,1,0,0],
        [0,1,1,1]]

print(RatMaze(matrix))