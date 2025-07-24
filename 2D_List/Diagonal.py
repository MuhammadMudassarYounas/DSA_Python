nums=[[1,2,3,],[4,5,6,],[7,8,9,]]
Rows=len(nums)
Columns=len(nums[0])
for i in range(0,Rows):
    for j in range(0,Columns):
        if i==j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
for i in range(0,Rows):
    j=2-i
    print(nums[i][j])
