#Example 2:  Single Number in Array Leet Code 136
#brute solution
num=[5,5,1,2,1,2,1,2,7,7,3]
def single(nums):
    dictionary={}
    for i in range(len(nums)):
        if nums[i] in dictionary:
            dictionary[nums[i]]+=1
        else:
            dictionary[nums[i]]=1
    if (dictionary[nums[i]]==1):
        return nums[i]
    #  for k in dictionary:
    # if dictionary[k]==1:
    #     return k 

print(single(num))

#optimal solution: using Xor Operation
nums=[5,5,1,2,1,2,7,7,3]
def SingleNumber(nums):
    ans =0
    for i in nums:
        ans =ans^ i
    return ans
print(SingleNumber(nums))
