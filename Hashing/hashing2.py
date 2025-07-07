n=[2,3,5,2,6,8,9,7,0,1,3,4,5,6,7,3,3]
m=[10,4,2,65,8,7,4,1,9]

hash_list={}
for num in n:
    if num in hash_list:
        hash_list[num]+=1
    else:
        hash_list[num]=1
for mum in m:
    if mum not in hash_list:
        print(0)
    else:
        print(hash_list[mum])