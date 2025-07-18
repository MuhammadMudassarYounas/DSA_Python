#Example 2: Array is sorted or not
num=[1, 2, 3, 4, 4, 5, 7, 7, 9]
def ArraySort(num):
    n=len(num)
    for i in range(0,n-1):
        if num[i]>num[i+1]:
            return False
        else:
            return True
print(ArraySort(num))