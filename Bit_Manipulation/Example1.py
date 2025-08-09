#Example 1: Minimum Bit flips to convert Number LeetCode 2220
def MinimumBitFlips(start,goal):
    ans=start^ goal
    count=0
    for i in range(0,32):
        if (ans &(1<<i)!=0):
            count+=1
    return count
print(MinimumBitFlips(10,7))
