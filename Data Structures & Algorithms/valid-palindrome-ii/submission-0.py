class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isplandirom(s):
            if(s==s[::-1]):
                return True
            else:
                return False

        for i in range(0,len(s)):
            t=s[0:i]+s[i+1:len(s)]
            r=isplandirom(t)  
            if(r==True):
                return True
        return False                  
        