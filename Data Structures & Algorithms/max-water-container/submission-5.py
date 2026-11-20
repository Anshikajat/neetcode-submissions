class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        m=0
        while(i<j):
            h=min(heights[i],heights[j])
            w=j-i
            if(m<h*w):
                m=h*w
            if(heights[i]<heights[j]):
                i+=1
            else:
                j-=1
        return m                
        