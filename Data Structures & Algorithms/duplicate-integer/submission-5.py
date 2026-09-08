class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        an=set()
        for i in range(len(nums)):
            if(nums[i] not in an):
                an.add(nums[i])
            else:
                return True
        return False            