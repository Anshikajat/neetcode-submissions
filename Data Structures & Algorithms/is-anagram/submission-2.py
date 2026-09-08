class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        an1={}
        an2={}
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            if(s[i] not in an1):
                an1[s[i]]=1
            else:
                an1[s[i]]+=1
            if(t[i] not in an2):
                an2[t[i]]=1
            else:
                an2[t[i]]+=1 
        if(an1==an2):
            return True
        return False               
