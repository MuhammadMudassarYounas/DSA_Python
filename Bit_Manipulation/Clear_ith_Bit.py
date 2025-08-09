def Set_ith_Bit(N,i):
    print(N & (~(1<<i))) #first shift the 1 with i and then take Not 
Set_ith_Bit(13,2)