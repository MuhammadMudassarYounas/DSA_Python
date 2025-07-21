num =[2,8,6,55,3,2,99,232,44,55,33,]
target=232
def linearSearching(num):
    for i in range(0,len(num)):
        if num[i]==target:
            return i    
    return -1
print(linearSearching(num))