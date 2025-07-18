# #Check Palindrome using loop
# s="nitinh"
# def Palindrome(s):
#     L=0
#     R=len(s)-1
#     while L <R:
#       if s[L]!=s[R]:
#         return False
#       L+=1
#       R-=1
#     return True
# print(Palindrome(s))

#Check Palindrome using recursion


s="nitinh"
def palindrome(s,l,r):
    if l>r:
        print("palindrome")
        return True
    if s[l]!=s[r]:
        print("not palindrome")
        return False
    return palindrome(s,l+1,r-1)
palindrome(s,0,len(s)-1)
