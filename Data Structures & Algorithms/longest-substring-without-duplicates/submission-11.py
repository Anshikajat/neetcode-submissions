class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h=set()
        l=0
        m=0
        for i in range(len(s)):
            while(s[i] in h):
                h.remove(s[l])
                l+=1
            h.add(s[i])    
            c=i-l+1     
             
            if(m<c):
                m=c
      
        return m        
        