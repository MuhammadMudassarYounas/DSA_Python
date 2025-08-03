num=[1,2,3,3,3,3,3,5,6,8,9,9,10]
def FirstLast(nums,target):
    low=0
    high=len(nums)-1
    first=-1
    last=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            first=mid
            high=mid-1
        else:
            low=mid+1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            last=mid
            high=mid-1
        else:
            low=mid+1
    return [first,last]
print(FirstLast(num,3))