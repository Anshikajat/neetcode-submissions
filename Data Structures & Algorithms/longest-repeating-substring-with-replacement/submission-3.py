class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h={}
        i=0
        l=0
        m=1
        res=0
        while(i<len(s)):
            if(s[i] not in h):
                h[s[i]]=1
            else:
                h[s[i]]+=1
                if(h[s[i]]>m):
                    m=h[s[i]]
            w=i-l+1
            if(w-m<=k):
                if(res<w):
                    res=w
            else:
                h[s[l]]-=1
                l+=1 
            i+=1
        return res               
                    
        
             
        