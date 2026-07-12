class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        a=0
        m=0
        l=0
        
        b = [0 for _ in range(len(height))]
        

        while(j>-1):
            if(height[j]>l):
                l=height[j]
            b[j]=l
            j=j-1     

    
        j=0   
        while(i<len(height)):
            if(m<height[i]):
                m=height[i]
            
            
            if(m>b[j]):
                a+=b[j]-height[i]
            else:
                a+=m-height[i]
            i=i+1 
            j=j+1
        return a                   


            
            


        