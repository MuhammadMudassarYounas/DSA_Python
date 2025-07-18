num=[3,7,9,5,4,2,1,7,4]
n=len(num)

for i in range(1,n):
    key = i
    j=i-1
    while j>=0 and num[j]>key:
        num[j+1]=num[j]
        j-=1
    num[j+1]=key
print(num)