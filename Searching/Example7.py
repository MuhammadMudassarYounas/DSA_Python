#Example 7: Rearrange Element By Sign
# Brute Solution 
num=[5,10,-3,-1,-10,6]
# def RearrangeElement(nums):
#     Positive=[]
#     Negative=[]
#     result=[]
#     for i in range(0,len(nums)):
#         if nums[i]>0:
#             Positive.append(nums[i])
#         else:
#             Negative.append(nums[i])
#     P=0
#     N=0
#     while P<len(Positive) and N<len(Negative):
#         result.append(Positive[P])
#         result.append(Negative[N])
#         P+=1
#         N+=1
#     return result
# print(RearrangeElement(num))
#Optimal Solution
def RearrangeElementSign(nums):
    n=len(nums)
    result=[0]*n
    P=0
    N=1
    for i in range(0,n):
        if nums[i]>=0:
            result[P]=num[i]
            P+=2
        else:
            result[N]=nums[i]
            N+=2
    return result
print(RearrangeElementSign(num))