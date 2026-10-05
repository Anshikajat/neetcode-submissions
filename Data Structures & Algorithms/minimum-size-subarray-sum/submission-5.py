class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        t=0
        res=float('inf')
        r=0
        l=0
        while(r<len(nums) and l<len(nums)):
            t+=nums[r]
            while t >= target:
                res = min(res, r - l + 1) # Update the minimum length found
                t -= nums[l]              # Subtract the left element
                l += 1   

                
                
                
                
            r+=1
        if(res==float('inf')):
            return 0        
        return res            

        