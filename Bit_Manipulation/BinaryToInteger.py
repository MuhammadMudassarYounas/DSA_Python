binary="1101"
def BinaryToInteger(x):
    integer=0
    power=0
    Index=len(x)-1
    while Index>=0:
        num=int(x[Index])*(2**power)
        integer+=num
        power+=1
        Index-=1
    return integer
print(BinaryToInteger(binary))    