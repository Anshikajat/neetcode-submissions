class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(t==""):
            return ""
        w={}
        h={}
        for i in t:
            if(i not in h):
                h[i]=1
            else:
                h[i]+=1
        have=len(h)
        need=0
        rl=[-1,-1]
        res=float('inf')
        l=0
        for j in range (len(s)):
            if(s[j] not in w):
                w[s[j]]=1
            else:
                w[s[j]]+=1
            if(s[j] in h and h[s[j]]==w[s[j]]):
                need+=1
            while(have==need):
                if((j-l+1) < res):
                    res=j-l+1
                    rl=[l,j]  
                w[s[l]]-=1
                if(s[l] in h and h[s[l]]>w[s[l]]):
                    need-=1
                l+=1
        if(res!=float('inf')):
            l,r=rl
            return s[l:r+1] 
        else:
            return ""               

        