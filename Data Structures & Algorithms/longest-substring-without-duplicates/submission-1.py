class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a={}
        i=0
        c=0
        m=0
        while(i<len(s)):
            if(s[i] not in a):
                a[s[i]]=i
                c=c+1
                i=i+1
            else:
                i=a[s[i]]+1
                a={}
                c=0
                
            if(m<c):
                m=c
        
        return m            

                   
        