#Use Head Recursion
print("Use Head Recursion")
def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)
func(1,5)
#use head recursion one parameter:
print("Use Head Recursion one parameter")
def func(n):
    if n==0:
        return
    print(n)
    func(n-1)
func(5)
#use Tail recursion:
print("use Tail recursion")
def func(i,n):
    if i>n:
        return
    func(i+1,n)
    print(i)
func(1,5)
#use Tail recursion one parameter:
print("use Tail recursion one paramter")
def func(n):
    if n==0:
        return
    func(n-1)
    print(n)
func(5)