class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        lm=height[i]
        rm=height[j]
        res=0
        while(i<j):
            if(height[j]<height[i]):
                j=j-1
                if(height[j]>rm):
                    rm=height[j]
                res+=rm-height[j]
            else:
                i=i+1
                if(height[i]>lm):
                   lm=height[i]
                res+=lm-height[i]
        return res        


        