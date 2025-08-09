num=[5,9,7]
def AllSequence(nums):
    Result=[]
    def solve(index,subSet):
        if index>=len(nums):
            Result.append(subSet.copy())
            return
        subSet.append(nums[index])
        solve(index+1,subSet)
        subSet.pop()
        solve(index+1,subSet)
    solve(0,[])
    return Result
print(AllSequence(num))