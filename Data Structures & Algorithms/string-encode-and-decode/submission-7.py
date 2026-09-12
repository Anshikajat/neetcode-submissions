class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            
            
            
            s+=str(len(i))+"#"+i 
        return s       
                


    def decode(self, s: str) -> List[str]:
        a=[]
        
        i=0
        while(i<len(s)):
            t=i
            while(s[t]!="#"):
               t+=1
            l=int(s[i:t])
            a.append(s[t+1:t+1+l])
            i=t+1+l                    



        return a            
            
