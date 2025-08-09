num=13
def IntegerToBinary(nums):
    Result=""
    while nums>0:
        if nums%2==1:
            Result+="1"
        else:
            Result+="0"
        nums=nums//2
    Result=Result[::-1]
    return Result

print(IntegerToBinary(num))