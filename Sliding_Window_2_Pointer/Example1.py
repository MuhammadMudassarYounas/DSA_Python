#Example 1:Longest Substring without repeating character leet code 3
#brute solution
def LongestSubstring(s):
    n=len(s)
    maxi=0
    for i in range(0,n):
        my_set=set()
        for j in range(i,n):
            if s[j] in my_set:
                break
            else:
                maxi=max(maxi,j-i+1)
                my_set.add(s[j])
    return maxi
print(LongestSubstring("CADBZABCD"))

def LongestSubStringCharacter(s):
    my_dic={}
    left=0
    right=0
    maxi=0
    n=len(s)
    while right<n:
        if s[right] in my_dic:
            left=max(left,my_dic[s[right]]+1)
        maxi=max(maxi,right-left+1)
        my_dic[s[right]]=right
        right+=1
    return maxi

print(LongestSubStringCharacter("CADBZABCD"))
