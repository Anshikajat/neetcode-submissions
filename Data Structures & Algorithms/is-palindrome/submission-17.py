class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i=0
        j=len(s)-1
        while(i<=j):
            while(s[i].isalnum()==False):
                if(i>=len(s)-1):
                    return True
                i+=1
                   
            while(s[j].isalnum()==False):
                if(j<=0):
                    break
                j-=1 
            
            if(s[i].lower()==s[j].lower()):
                i+=1
                j-=1
            else:
                return False
        return True                   