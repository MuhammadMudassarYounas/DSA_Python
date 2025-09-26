#make heapify Algorithm   
def HeapifyAlgo(index,arr,val):
    if arr[index]>val:
        arr[index]=val
        heapifyDown(arr,index)
    else:
        arr[index]=val
        heapifyUp(arr,index)
    return arr




def heapifyDown(arr,index):
        n=len(arr)

        largest_index=index

        leftChild=2*index+1
        RightChild=2*index+2

        if leftChild<n and arr[leftChild]>arr[largest_index]:
            largest_index=leftChild

        if RightChild<n and arr[RightChild]>arr[largest_index]:
            largest_index=RightChild
        
        if largest_index != index:
            arr[largest_index] , arr[index]= arr[index],arr[largest_index]
            heapifyDown(arr,largest_index)


def heapifyUp(arr,index):
    n=len(arr)
    parentIndex= (index-1)//2

    if index>0 and arr[parentIndex]<arr[index]:
        arr[parentIndex],arr[index]=arr[index],arr[parentIndex]
        heapifyUp(arr,parentIndex)

print(HeapifyAlgo(7,[10,7,6,4,5,4,5,3,2,],15))