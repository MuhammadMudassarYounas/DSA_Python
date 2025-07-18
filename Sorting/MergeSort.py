num=[3,7,9,5,4,2,1,7,4]
n=len(num)

def MergeSort(num):
    if len(num)<=1:
        return num
    mid = len(num)//2
    left_array=num[:mid]
    right_array=num[mid:]
    left=MergeSort(left_array)
    right=MergeSort(right_array)
    return Merge_array(left,right)

def Merge_array(L,R):
    result=[]
    i,j=0,0
    n,m=len(L),len(R)
    while i<n and j<m:
        if(L[i]<=R[j]):
          result.append(L[i])
          i+=1
        else:
            result.append(R[j])
            j+=1
    if(i<n):
        while i<n:
            result.append(L[i])
            i+=1
    if(j<m):
        while j<m:
            result.append(R[j])
            j+=1
    return result

print(MergeSort(num))

