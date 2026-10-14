class Solution:
    def simplifyPath(self, path: str) -> str:
        s=[]
        i=0
        while(i<len(path)):
            p=""
            if(path[i]=="/"):
                j=i+1
                while(j<len(path) and path[j]!="/"):
                    p+=path[j]
                    j+=1
                i=j    
            if(p==".."):
                if(s):
                   s.pop()
                continue
            elif(p=="."):
                continue
            else:
                if(p!=""):
                   s.append(p)
        return "/"+"/".join(s)                
                

        