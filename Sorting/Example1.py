#Example 1:Largest number in array
num=[55, 6,333,99,77,-55,1111,22,]

largest_Number=num[0]
S_LargestNumber=float("-inf")
for i in range(0,len(num)-1):
    if largest_Number<=num[i]:
        largest_Number=num[i]
for i in range(0,len(num)-1):
    if num[i]>S_LargestNumber and num[i]!=largest_Number:
        S_LargestNumber=num[i]
print("largest_Number",largest_Number)
print("Second Largest Number",S_LargestNumber)

