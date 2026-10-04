class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k=0
        m=0
        i=0
        p=0
        h=set()
        while(i<len(s)):
            if(s[i] not in h):
                h.add(s[i])
                k+=1
        
                if(m<k):
                    m=k
            else:
                while(s[i] in h):
                    h.remove(s[p])
                    p+=1
                    k-=1
                h.add(s[i]) 
                k+=1
                
      
            i+=1
        return m                    
        