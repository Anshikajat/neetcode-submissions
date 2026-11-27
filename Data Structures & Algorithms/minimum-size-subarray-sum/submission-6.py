class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float('inf')
        l=0
        s=0
        for i in range(len(nums)):
            s+=nums[i]
        
            while(s>=target):
                res=min(res,i-l+1)
                s-=nums[l]
                l+=1
        if(res==float('inf')):
            return 0        
        return res        
        