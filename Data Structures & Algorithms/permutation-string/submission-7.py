class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        h={}
        h1={}
        for i in range(97,123):
            h[chr(i)]=0
            h1[chr(i)]=0
        for i in range(len(s1)):
            h[s1[i]]+=1
        l=0
        
        for r in range(len(s2)):
        
            h1[s2[r]]+=1
            if(r-l+1==len(s1)):
                if(h1==h):
                    return True
                else:
                    h1[s2[l]]-=1
                    l+=1
        return False                   


            

        

    