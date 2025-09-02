#Example 3:Minimum Number of Coin //geek for geek 
def MinimumCoin(coins,N):
    n=len(coins)
    result=[]
    for i in range(n-1,-1,-1):
        while N>=coins[i]:
            result.append(coins[i])
            N-=coins[i]
    return result
print(MinimumCoin([1,2,3,5,10,20,50,100,200,2000],47))