num=[3,7,9,5,4,2,1,7,4]
n=len(num)
def Bubble_Sort(num):
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    return num
print(Bubble_Sort(num))