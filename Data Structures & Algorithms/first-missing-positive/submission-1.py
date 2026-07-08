class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m=0
        
        a=set()
        for i in range(0,len(nums)):
            if(nums[i] not in a):
                a.add(nums[i])
                if(nums[i]>m):
                    m=nums[i]
        p=m        
        if(1 not in a):
            return 1
        for i in range(0,len(nums)):
            if(nums[i]+1 not in a and nums[i]>0):
                if(m>nums[i]+1):
                    m=nums[i]+1
        if(m==p):
            return m+1
        else:
            return m     
                                      

        