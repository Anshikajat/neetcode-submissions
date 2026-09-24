class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(t==""):
            return ""
        h1={}
        h2={}
        for i in t:
            if(i not in h1):
                h1[i]=1
            else:
                h1[i]+=1
        have=0
        need=len(h1)
        l=0
        re=[-1,-1]
        res=float('inf')
        for j in range(len(s)):
            if(s[j] not in h2):
                h2[s[j]]=1
            else:
                h2[s[j]]+=1
            if(s[j] in h1 and h2[s[j]]==h1[s[j]]):
                have+=1
            while(have==need):
                if(j-l+1<res):
                    res=j-l+1
                    re=[l,j]
                h2[s[l]]-=1
                if(s[l] in h1 and h2[s[l]]<h1[s[l]]):
                    have-=1
                l+=1   
        l,j=re
        if(res!=float('inf')):
            return s[l:j+1]
        else:
            return ""    



            

                

        