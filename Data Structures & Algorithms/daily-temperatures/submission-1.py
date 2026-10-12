class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        p=[0]*len(temperatures)
        s=[]
        for i in range(len(temperatures)):
             while(s and s[-1][0]<temperatures[i]):
                p[s[-1][1]]=i-s[-1][1]
                s.pop()
                
                
             s.append((temperatures[i],i))
        return p        