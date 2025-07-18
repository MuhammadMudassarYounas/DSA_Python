#use parameter recursion
def sum(s,i,n):
    if i>n:
        print(s)
        return
    sum(s+i,i+1,n)
sum(0,1,10)
#use functional recursion
def func(n):
    if n==1:
        return 1
    return n+func(n-1)
print(func(10))