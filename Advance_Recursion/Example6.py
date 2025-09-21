#Example 6: Combination Sum 3 Leet code 216

def Combination(k,n):
    result=[]
    def backtrack(last ,total,subset):
        if total==n and len(subset)==k:
            result.append(subset.copy())
            return
        if total>n or len(subset)>=k:
            return
        for i in range(last, 10):
            sum=total+i
            subset.append(i)
            backtrack(i+1,sum,subset)
            subset.pop()

    backtrack(1,0,[])
    return result
print(Combination(3,8))