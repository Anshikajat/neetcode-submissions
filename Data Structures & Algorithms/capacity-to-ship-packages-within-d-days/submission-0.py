class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=0
        r=0
        for i in weights:
            if(i>l):
                l=i
            r+=i
        res=r    
        def shiping(m):
            s=1
            cu=m
            for i in weights:
                if(cu-i<0):
                   s+=1
                   cu=m
                cu-=i
            return s<=days    
                    
        while(l<=r):
            m=(l+r)//2
            if(shiping(m)):        
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res            