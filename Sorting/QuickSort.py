num=[3,7,9,5,4,2,1,7,4]
def QuickSort(num,Low,high):
    if Low<high:
          p_index=Partition(num,Low,high)
          QuickSort(num,Low,p_index-1)
          QuickSort(num,p_index+1,high)
    return num

def Partition(num,Low,high):
    Pivot=num[Low]
    i=Low + 1
    j=high
    while i<j:
        while num[i]<=Pivot and i<=high-1:
               i+=1
               
        while num[j]>=Pivot and j>=Low+1:
               j-=1
        if i<j:
           num[i],num[j]=num[j],num[i]
    num[Low],num[j]=num[j],num[Low]
    return j

x=QuickSort(num,0,len(num)-1)
print(x)             