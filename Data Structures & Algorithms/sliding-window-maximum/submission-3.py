class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        a=[]
        
        s=[]
        l=0
        r=0
        while(r<len(nums)):
            while(a and nums[a[-1]]<nums[r]):
                a.pop()
            a.append(r) 
            if(r-l+1==k):
                

                s.append(nums[a[0]])
                l+=1
                if(a[0]<l):
                    a.pop(0)

                
            r+=1    
        return s               


        