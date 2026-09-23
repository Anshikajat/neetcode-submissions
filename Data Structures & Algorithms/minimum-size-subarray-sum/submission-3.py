class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        res=float('inf')
        l=0
        for i in range(len(nums)):
            sum+=nums[i]
            while(sum>=target):
                if(res>i-l+1):
                    res=i-l+1
                sum-=nums[l]
                l+=1
        if(res==float('inf')):
            return 0
        return res        
        

        