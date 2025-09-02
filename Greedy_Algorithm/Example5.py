#Example 5: N Meeting in Room  //GFG problem
class Meeting:
    def __init__(self,start,end,position):
        self.start=start
        self.end=end
        self.position=position
def N_Meeting(start,end):
    n=len(start)
    meet=[Meeting(start[i],end[i],i+1) for i in range(0,n)]
    meet.sort(key= lambda x:(x.start,x.end))
    result=[]
    count=1
    result.append(meet[0].position)
    lastTime=meet[0].end
    for i in range( 1,n):
        if meet[i].start>lastTime:
            count+=1
            result.append(meet[i].position)
            lastTime=meet[i].end
    return result,count
print(N_Meeting([1,3,0,5,8,5],[2,6,7,3,9,9,],))
