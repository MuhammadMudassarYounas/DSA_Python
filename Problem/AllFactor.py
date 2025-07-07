#brute solution
num = 20
result=[]
for i in range(1,num+1):
    if num%i==0:
        result.append(i)
print("The Factor of this number is: use brute approach",result)
#use better approach
number=10
final_result=[]
for i in range(1,num//2):
    if number%i==0:
        final_result.append(i)
final_result.append(number)
print("The Factor of this number is:Use better approach",final_result)

#use optimal solution
from math import sqrt
n=17
optimal_result=[]
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        optimal_result.append(i)
        if n//i !=i:
            optimal_result.append(n//i)
print("The Factor of this number is:Optimal solution",optimal_result)

