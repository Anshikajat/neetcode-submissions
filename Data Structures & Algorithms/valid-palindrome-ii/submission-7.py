class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        f=0
        def isplaindrom(k,m):
            while(k<=m):
                if(s[k]!=s[m]):
                    return False
                k=k+1
                m-=1
            return True        
        while(i<=j):
            if(s[i]==s[j]):
                j=j-1
                i=i+1
            else:
                if(isplaindrom(i+1,j)):
                    return True
                    
                elif(isplaindrom(i,j-1)):
                    return True
                else:
                    return False
        return True            
                   

        