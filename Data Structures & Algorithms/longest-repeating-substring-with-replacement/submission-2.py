class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m=0
        l=0
        r=0
        h={}
        res=0
        while(r<len(s)):
            if(s[r] not in h):
                h[s[r]]=1
            else:
                h[s[r]]+=1
            if(m<h[s[r]]):
                m=h[s[r]]
            if(((r-l+1)-m)<=k):
                res=r-l+1
            else:
                h[s[l]]-=1
                l+=1
                
            r+=1
        return res                            

            
        