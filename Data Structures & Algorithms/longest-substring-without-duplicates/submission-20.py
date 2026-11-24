class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==1):
            return 1
        i=0
        h={}
        res=0
        for j in range(len(s)):
            if(s[j] in h):
                if(h[s[j]]<i):
                    res=max(res,j-i+1)
                    h[s[j]]=j
                else:
                    res=max(res,j-i)
                    i=h[s[j]]+1 
                    h[s[j]]=j
            else:
                h[s[j]]=j
                res=max(res,j-i+1)    
        return res               



        