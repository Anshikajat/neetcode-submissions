class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if(i.lstrip("-").isdigit()):
                s.append(int(i))
            else:
                a=s.pop()
                b=s.pop()
                if(i=="+"):
                    s.append(a+b)
                elif(i=="-"):
                    s.append(b-a)
                elif(i=="*"):
                    s.append(a*b)

                else:
                    s.append(int(b/a)) 
        return int(s[-1])                   
                        
        