Arr=[4,20,9,12,16,13,19,21]
def ArrayIsMinHeap(arr):
    n=len(arr)
    internal=(n//2)-1
    for i in range(internal,-1,-1):
        left=2*i-1
        right=2*i-2

        if arr[i]>arr[left]:
            return False
        if arr[i]>arr[right]:
            return False
    return True


print(ArrayIsMinHeap(Arr))