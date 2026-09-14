class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h=set(nums)
        
        c=0
        for i in range(len(nums)):
            if(nums[i]-1 in h):
                continue
            j=1
            a=1
            while(nums[i]+j in h):
                j=j+1
                a+=1
            if(a>c):
                c=a
        return c            

           

        