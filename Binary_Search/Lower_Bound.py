num=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
def LowerBOund(nums,target):
    lowerIndex=-1
    low=0
    high=len(nums)-1
    while low<=high:
        mid =(low+high)//2
       
        if nums[mid] >=target:
            lowerIndex=mid
            high=mid-1
          
        else:
            low=mid+1  
    return lowerIndex
print(LowerBOund(num,1))
