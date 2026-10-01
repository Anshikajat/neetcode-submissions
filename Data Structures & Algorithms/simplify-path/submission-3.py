class Solution:
    def simplifyPath(self, path: str) -> str:
        s=[]
        p=""
        path+="/"
        i=0
        while(i<len(path)):
    
             
            if(path[i]!="/"):
                p+=path[i]
                i+=1
                print("p",p)
            elif(path[i]=="/"):
                if(p==".."):
                    if(len(s)>=2):
                        s.pop()
                        s.pop()
                    else:
                        s.pop() 
                    p=""     
                elif(p=="."):
                    
                    p="" 
                elif p:
                        s.append(p)
                        s.append("/")
                        p = ""

                    # Now handle /
                if not s:
                    s.append("/")
                
                i += 1
                
        if len(s) > 1 and s[-1] == "/":
            s.pop()        
        return("".join(s))                    


        