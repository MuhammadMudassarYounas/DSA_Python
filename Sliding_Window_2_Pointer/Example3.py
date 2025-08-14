#Example 3:Fruits in Basket leet code 904
#brute solution
def FruitsInBasket(nums):
    n=len(nums)
    maxi=0
    for i in range(0,n):
        my_set=set()
        for  j in range (i,n):
            my_set.add(nums[j])
            if len(my_set)>2:
                break
            maxi=max(maxi,j-i+1)
    return maxi
#better solution
def Fruits_In_Basket(nums):
    maxi=0
    n=len(nums)
    left=0
    right=0
    my_dic={}
    while right<n:
        my_dic[nums[right]]=my_dic.get(nums[right],0)+1
        while len(my_dic)>2:
            my_dic[nums[left]]-=1
            if my_dic[nums[left]]==0:
                del my_dic[nums[left]]
            left+=1
        if len(my_dic)<=2:
            maxi=max(maxi,right-left+1)
            right+=1
    return maxi 
         
#optimal solution
def Fruit_In_Basket(nums):
    maxi=0
    n=len(nums)
    left=0
    right=0
    my_dic={}
    while right<n:
        my_dic[nums[right]]=my_dic.get(nums[right],0)+1
        if len(my_dic)>2:
            my_dic[nums[left]]-=1
            if my_dic[nums[left]]==0:
                del my_dic[nums[left]]
            left+=1
        if len(my_dic)<=2:
            maxi=max(maxi,right-left+1)
            right+=1
    return maxi 


print(FruitsInBasket([3,3,3,1,2,1,1,2,3,3,4]))
print(Fruits_In_Basket([3,3,3,1,2,1,1,2,3,3,4]))
print(Fruit_In_Basket([3,3,3,1,2,1,1,2,3,3,4]))
