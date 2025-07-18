nums = [1,2,3,4,5,6,7,8,9]

def fun(num,l,r):
    if l>=r:
        return
    nums[l],nums[r]=nums[r],nums[l]
    fun(num,l+1,r-1)
(fun(nums,0,len(nums)-1))
print(nums)

#reverse the list using while loop
l=0
r=len(nums)-1
while l<r:
    nums[l],nums[r]=nums[r],nums[l]
    l+=1
    r-=1
print(nums)
