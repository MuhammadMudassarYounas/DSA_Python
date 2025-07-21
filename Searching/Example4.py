#Two Sum problem 
#Brute solution
num=[5,9,1,2,4,15,6,3]
target=13
def TwoSum(num):
    for i in range(0,len(num)):
        for j in range(1,len(num)):
            if(num[i]+num[j]==target):
                return [i ,j]
print(TwoSum(num))
#Optimal solution
def TwoSumProblem(num,n):
    hash_map={}
    for i in range(0,len(num)):
        remaining=n-num[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[num[i]]=i
print(TwoSumProblem(num,target))