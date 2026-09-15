class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        if(len(s)==1):
            return True
        while(i<j):
            while(s[i].isalnum()==False):
                i=i+1
                if(i>len(s)-1):
                    return True
               
            while(j>-1 and s[j].isalnum() == False):
                j=j-1
          
            if(s[i].lower()!=s[j].lower()):
                return False    
            if(s[i].lower()==s[j].lower()):
                i=i+1
                j=j-1
        return True