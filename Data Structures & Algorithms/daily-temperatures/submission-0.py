class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        p=[]
        for i in range(len(temperatures)-1,-1,-1):
            while(s and s[-1][0]<=temperatures[i]):
                s.pop()
            if(not s):
                p.append(0)
            else:        
                p.append(s[-1][1]-i)
            s.append((temperatures[i],i))
        return p[::-1]        

        