class Solution:
    def mySqrt(self, x: int) -> int:
        s=1
        l=x
        while(s<=l):
            m=(s+l)//2
            if(m*m==x):
                return m
            elif(m*m<x):
                s=m+1
            else:
                l=m-1
        if(s*s>x):        
           return s-1 
        return s                   