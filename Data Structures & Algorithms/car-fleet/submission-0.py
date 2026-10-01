class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a=[]
        s=[]
        for i in range(len(position)):
            a.append((position[i],speed[i]))
        a.sort(reverse=True)
        for p,t in a:
            s.append((target-p)/t)
            if(len(s)>=2 and s[-2]>=s[-1]):
                s.pop()
        return len(s)        



            
        