class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # u=sorted(s)
        # p=sorted(t)
        # if(p==u):
        #     return True
        # else:
        #     return False    
        a={}
        b={}
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            if(s[i] in a):
                a[s[i]]+=1
            if(s[i] not  in a):
                a[s[i]]=1
            if(t[i] in b):
                b[t[i]]+=1
            if(t[i] not in b):
                b[t[i]]=1 
        print(a,b)        
        if(a==b):
            return True
        return False                  

        