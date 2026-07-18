class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        l=0
        c=0
        a=0
        t=0
        p = float('inf')
        
        for i in range(len(nums)):
            c+=nums[i]
        
            while(c>=target):
                c-=nums[l]
                if(p>i-l+1):
                    p=i-l+1
                t=1
                l=l+1
        if(t==1):
            return p 
        else:
            return 0    

