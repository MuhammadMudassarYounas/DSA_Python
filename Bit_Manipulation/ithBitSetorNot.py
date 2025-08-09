def BitSetOrNot(binary,n):

    # shift=1<<n
    # ans=int(binary) & shift
    # if ans ==0:
    #     return False
    # else:
    #     return True
    if ((binary >> n )& 1)!=0:
        return True
    else:
        return False
print(BitSetOrNot(13,2))