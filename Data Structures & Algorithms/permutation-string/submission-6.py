class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        i=0
        h={}
        for p in range(len(s1)):
            if(s1[p] not in h):
                h[s1[p]]=1
            else:
                h[s1[p]]+=1

        while(i<len(s2)-k+1):
    
            j=i
            h2={}
            while(j<i+k):
                if(s2[j] not in h2):
                    h2[s2[j]]=1
                else:
                    h2[s2[j]]+=1
                j+=1    
                   
            if(h==h2):
                return True

            i+=1

        return False