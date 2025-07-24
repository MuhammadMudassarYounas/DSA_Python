#Example 4:3Sum Problem LeetCode 15
#brute Solution
num=[-1,0,1,2,-1,-4]
def Sum(nums):
    Result=set(())
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+num[k]==0:
                    Arr=[nums[i],nums[j],nums[k]]
                    Arr.sort()
                    Result.add(tuple(Arr))
    return [list(ans) for ans in Result]
print(Sum(num))
#optimal solution:
Arr = [-2, -2, -1, -2, -1, -1, 0, 0, 2, 0, 2, 2]

def ThreeSum(Arr):
    Result = []
    Arr.sort()
    n = len(Arr)

    for i in range(n):
        if i > 0 and Arr[i] == Arr[i - 1]:
            continue  # skip duplicate i values

        j = i + 1
        k = n - 1

        while j < k:
            total = Arr[i] + Arr[j] + Arr[k]

            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                Result.append([Arr[i], Arr[j], Arr[k]])
                j += 1
                k -= 1

                # ✅ skip duplicate j values
                while j < k and Arr[j] == Arr[j - 1]:
                    j += 1
                # ✅ skip duplicate k values
                while j < k and Arr[k] == Arr[k + 1]:
                    k -= 1

    return Result

print(ThreeSum(Arr))