class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        u=sorted(s)
        p=sorted(t)
        if(p==u):
            return True
        else:
            return False    
        