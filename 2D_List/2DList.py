#Explain 2D List and Matrix
num=[[1,2,3],[4,5,6],[7,8,9]]
print(num)
#print Specific element
print(num[1][1])
#print Number of rows
print("Row in Matrix",len(num))
#print Number of column
print("Column in Matrix",len(num[0]))

nums=[[1,2,3,4,5,6],[4,5,6,7,8,9],[7,8,9,10,11,12]]
print("Number of Rows in Matrix",len(nums))
print("Number of Column in Matrix",len(nums[0]))
column=len(nums[0])
for i in range(0,len(nums)):
    for j in range(0,column):
        print(nums[i][j],end="  ")
    print()
for i in range(0,column):
    for j in range(0,len(nums)):
        print(nums[j][i],end="  ")
    print()