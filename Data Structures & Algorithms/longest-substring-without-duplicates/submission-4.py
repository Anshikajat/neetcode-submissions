class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a={}
        i=0
        m=0
        j=0
        while(i<len(s)):
            if(s[i] in a and a[s[i]]>=j):
                j=a[s[i]]+1
                
            a[s[i]]=i
            p=i-j+1
            if(m<p):
                m=p   
            i=i+1    
        
        return m            

                   
        