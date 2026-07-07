class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0

        for i in range(0,len(nums)):
            if(nums[i]!=nums[i-1]):
                nums[k]=nums[i]
                k=k+1
            
        if(len(nums)==1):
            return 1
        return k  


        