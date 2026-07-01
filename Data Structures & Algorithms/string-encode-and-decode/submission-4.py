class Solution:

    def encode(self, strs: List[str]) -> str:
        e=""
        d=[]
        for i in strs:
            
            for j in i:

                e=e+chr((ord(j)+1))
            e=e+" "    
              
        return e 


    def decode(self, s: str) -> List[str]:
        d=[]
        p=""
        for i in s:
            if(i==" "):
                d.append(p)
                p=""
                continue
        
            p=p+chr((ord(i)-1))

               
        return d
