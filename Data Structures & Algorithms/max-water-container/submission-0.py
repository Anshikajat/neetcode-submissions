class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        a=0
        while(i<j):
            w=j-i
            if(heights[i]<heights[j]):
                h=heights[i]
                i=i+1
            else:
                h=heights[j]
                j=j-1
            if(a<h*w):
                a=h*w
        return a        
                    
                    
        