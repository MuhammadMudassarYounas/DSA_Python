number=[2,1,2,3,4,5,3,2,1,3,4,2,2,]
freq_map={}
for i in range(0,len(number)):
    if number[i] in freq_map:
        freq_map[number[i]]+=1
    else:
        freq_map[number[i]]=1
print("The Frequency of number in list:",freq_map)

#use hash get method

hash_map={}
for i in range(0,len(number)):
    hash_map[number[i]]=hash_map.get(number[i],0)+1
print("The Frequency of number in list:using get method",hash_map)