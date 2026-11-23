class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        ml=height[i]
        mr=height[j]
        c=0
        while(i<j):
           if(ml<mr):
            i+=1
            ml=max(ml,height[i])
            c+=ml-height[i]
           else:
            j-=1
            mr=max(mr,height[j])
            c+=mr-height[j] 
        return c                    

            
        