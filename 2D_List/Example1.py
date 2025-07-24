#Example 1:Set Matrix Zero leetCode 73
#Brute Solution
nums=[[1,2,3,4],[5,6,0,7],[8,0,9,1],[2,3,4,5]]
# def SetMatrix(nums):
#     Rows=len(nums)
#     Columns=len(nums[0])
#     for i in range(0,Rows):
#         for j in range(0,Columns):
#             if nums[i][j]==0:  
#              return  SetInfinite(nums,i,j)
#     for i in range(0,Rows):
#         for j in range(0,Columns):
#             if nums[i][j]==float("inf"):
#                 nums[i][j]=0
# def SetInfinite(nums,row,col):
#     Rows=len(nums)
#     Columns=len(nums[0])
#     for i in range(0,Rows):
#         if nums[i][col]!=0:
#             nums[i][col]=float("inf")
#     for j in range(0,Columns):
#         if nums[row][j]!=0:
#             nums[row][j]=float("inf")
#     return nums

# print(SetMatrix(nums))

#optimal solution
def SetZero(nums):
    Rows=len(nums)
    Columns=len(nums[0])
    RowTrack=[0 for i in range(Rows)]
    ColumnTrack=[0 for j in range(Columns)]
    for i in range(0,Rows):
        for j in range(0,Columns):
            if nums[i][j]==0:
                RowTrack[i]=-1
                ColumnTrack[j]=-1

    for i in range(0,Rows):
        for j in range(0,Columns):
            if RowTrack[i]==-1 or ColumnTrack[j]==-1:
                nums[i][j]=0
    return nums
print(SetZero(nums))
