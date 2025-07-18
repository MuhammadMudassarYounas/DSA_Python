#Example 3: Remove duplicate from sorted array
num=[1,1,1,2,3,4,4,5,5,5,4,3,6,7,7,9]
unique_list=[]
for i in range(0,len(num)):
    if num[i] not in unique_list:
        unique_list.append(num[i])
n=len(unique_list)
print(unique_list,n)