#Example 5: Subset Sum // GFG
def SubSetSum(nums):
    result=[]
    def backtrack(index,total):
        if index>=len(nums):
            result.append(total)
            return
        sum=total+nums[index]
        backtrack(index+1,sum)
        sum=total
        backtrack(index+1,sum)
    backtrack(0,0)
    return result

print(SubSetSum([5,9,3]))
