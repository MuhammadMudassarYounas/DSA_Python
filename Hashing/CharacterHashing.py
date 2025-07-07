#use for only Small Alphabat
s="amksiuegdjfdgidvdxyza"
q="axywkdkfgd"

hash_list=[0]*26
for i in s:
    assci=ord(i)
    index=assci-97
    hash_list[index]+=1
print(hash_list)
for j in q:
    idx =ord(j) -97
    print(hash_list[idx])

#use for Small and Large Alpabat

s="aAmksiuegdjFdgidvDxyza"
q="axywkdkFgd"

hash_map=[0]*127
for i in s:
    assci=ord(i)
    hash_map[assci]+=1
for j in q:
    idx=ord(j)
    print(hash_map[idx])
