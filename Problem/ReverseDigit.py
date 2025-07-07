n=1234
num =n
result=0
while num>0:
    last_digit=num%10
    result=(result*10)+last_digit
    num =num//10
if n==result:
    print("The Given number is Palindrome")
else:
    print("The number is not Palindrome")