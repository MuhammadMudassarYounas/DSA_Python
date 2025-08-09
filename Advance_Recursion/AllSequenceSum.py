num=[5,9,3,4,1]
#Brute solution 
def AllSequenceSum(nums,target):
    Result=[]
    def solve(index,subSet):
        if index>=len(nums):
            if sum(subSet)==target:    
                Result.append(subSet.copy())
            return
        subSet.append(nums[index])
        solve(index+1,subSet)
        subSet.pop()
        solve(index+1,subSet)
    solve(0,[])
    return Result
print(AllSequenceSum(num,9))

#optimal Solution
def AllSequenceSumK(nums,target):
    Result=[]
    def solve(index,total,subset):
        if total==target:
            Result.append(subset.copy())
            return
        elif total>target:
            return
        if index>=len(nums):
            return
        subset.append(nums[index])
        sum=total+nums[index]
        solve(index+1,sum,subset)
        e=subset.pop()
        sum-=e
        solve(index+1,sum,subset)
    solve(0,0,[])
    return Result
print(AllSequenceSumK(num,9))
