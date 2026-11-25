class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m=0
        l=0
        res=0
        h={}
        for i in range(len(s)):
            if(s[i] not in h):
                h[s[i]]=1
            else:
                h[s[i]]+=1

            m=max(m,h[s[i]])    
            while((i-l+1-m)>k):
                h[s[l]]-=1
                l+=1
            res=max(res,i-l+1)    
        return res    




        