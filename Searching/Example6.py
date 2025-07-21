#Example 6:Best Time to Buy & Sell Stock
#Brute Solution 
nums=[8,7,6,5,4,3,2,1]
def BuySell(nums):
    maxi=0
    for buy in range(0,len(nums)-1):
        for sell in range(buy+1,len(nums)):
            total=nums[sell]-nums[buy]
            if(total>maxi):
                maxi=total
            if(maxi<0):
                return 0
    return maxi
print(BuySell(nums))

#optimal solution
def BestBuySell(nums):
    min=float("inf")
    max=0
    for i in range(0,len(nums)):
        if nums[i]<min:
            min=nums[i]
        max=nums[i]-min
        if max<0:
            return 0
    return max
print(BestBuySell(nums))

            
