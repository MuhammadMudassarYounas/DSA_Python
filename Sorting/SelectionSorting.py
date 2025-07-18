#Acceding order
num=[3,7,9,5,4,2,1,7,4]
def selection_Sort(num):
    for i in range(0,len(num)):
        min_index=i
        for j in range(i+1,len(num)):
            if num[j]<num[min_index]:
                min_index=j
        num[i],num[min_index]=num[min_index],num[i]
    return num
Sorted_array=selection_Sort(num)
print(Sorted_array)
#decceding order
num=[3,7,9,5,4,2,1,7,4]
def selection_Sort(num):
    for i in range(0,len(num)):
        min_index=i
        for j in range(i+1,len(num)):
            if num[j]<num[min_index]:
                min_index=j
        num[i],num[min_index]=num[min_index],num[i]
    return num
Sorted_array=selection_Sort(num)
print(Sorted_array)
