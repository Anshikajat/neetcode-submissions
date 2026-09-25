class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        if(len(s)==1):
            return False
        for i in s:
            
            if(i=="(" or i=="{" or i=="["):
                a.append(i)

            elif(i==")"):
                if(len(a)==0):
                    return False
                p=a.pop()
                if(p!="("):
                    return False
            elif(i=="]"):
                if(len(a)==0):
                    return False
                p=a.pop()
                if(p!="["):
                    return False  
            else:
                if(len(a)==0):
                    return False
                p=a.pop()
                if(p!="{"):
                    return False             

        if(len(a)>0):
            return False
        return True    

                
        