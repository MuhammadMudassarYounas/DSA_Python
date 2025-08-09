num=[1,3,2,1]
#brute solution
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
    return len(Result)
print(AllSequenceSumK(num,3))

#optimal solution
def CountAllSequence(nums,target):
    def BackTrack(index,total):
        if total==target:
            return 1
        elif total>target:
            return 0
        if index>=len(nums):
            return 0
        sum=total+nums[index]
        pick=BackTrack(index+1,sum)
        sum=total
        not_pick=BackTrack(index+1,sum)
        return pick + not_pick
    print(BackTrack(0,0))
CountAllSequence(num,3)
