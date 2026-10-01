class Solution:
    def decodeString(self, s: str) -> str:
        p=[]
        i=0
        t=""
        while(i<len(s)):
            if(s[i]=="]"):
                t=""
                while(p[-1]!="["):
                    t=p.pop()+t
                p.pop()
                k=""
                while(p and p[-1].isdigit()):
                    k=p.pop()+k
                p.append(int(k)*t)    


            else:
                p.append(s[i])
            i+=1    
        return "".join(p)                
        