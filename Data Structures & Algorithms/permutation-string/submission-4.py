class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d={}
        e={}
        for i in s1:
            if(i in d):
                d[i]=d[i]+1
            else:
                d[i]=1
        j=0         
        for i in range(len(s2)):
            if(s2[i] in e):
                e[s2[i]]=e[s2[i]]+1
            else:
                e[s2[i]]=1
            if((i-j+1)>len(s1)):
                if(e[s2[j]]>1):
                    e[s2[j]]-=1
                else:
                    del e[s2[j]]   
                j+=1
            if(i-j+1==len(s1)):
                if(d==e):
                    return True    
            
                
                    
        return False                           

        