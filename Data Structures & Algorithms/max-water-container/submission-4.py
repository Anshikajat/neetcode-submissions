class Solution:
    def maxArea(self, heights: List[int]) -> int: 
        i=0
        p=0
        j=len(heights)-1
        res=0
        while(i<j):
            if(heights[i]>heights[j]):
                if(res<(heights[j]*(j-i))):
                    res=heights[j]*(j-i)
                j=j-1
            else:
                if(res<(heights[i]*(j-i))):
                    res=heights[i]*(j-i)
                i=i+1    
                
               
   
        return res      


        