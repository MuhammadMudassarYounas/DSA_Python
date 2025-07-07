n=[2,3,5,2,6,8,9,7,0,1,3,4,5,6,7,3,3]
m=[10,4,2,65,8,7,4,1,9]

hash_list=[0]*10
for num in n:
    hash_list[num]+=1
print(hash_list)
for number in m:
    if number > 9 or number <0:
        print(0)
    else:
        print(hash_list[number])
        