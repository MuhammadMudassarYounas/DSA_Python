#Example 2:Fractional Knapsack geek for geek
class Item:
    def __init__(self,v,w):
        self.v=v
        self.w=w
        self.r=v//w
def knapsack(objs,cap):
    objs.sort(key=lambda x:x.r,reverse=True)
    totalValue=0
    for i in objs:
        if cap>=i.w:
            cap-=i.w
            totalValue+=i.v
        else:
            totalValue+=i.r*cap
            break
    return totalValue
        

items=[Item(100,20),Item(60,10),Item(100,50),Item(200,50)]
bag_Cap=90
print("Max Value" ,knapsack(items,bag_Cap))