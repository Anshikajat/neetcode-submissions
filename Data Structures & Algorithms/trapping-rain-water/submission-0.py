class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        a=0
        m=0
        
        while(i<len(height)):
            if(m<height[i]):
                m=height[i]
            j=len(height)-1
            l=height[i]    
            while(j>i):
                if(height[j]>l):
                    l=height[j]
                j=j-1
            if(m>l):
                a+=l-height[i]
            else:
                a+=m-height[i]
            i=i+1 
        return a                   


            
            


        