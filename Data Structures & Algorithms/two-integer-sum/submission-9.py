class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        for i in range(len(nums)):
            a=target-nums[i]
            if(a in has):
                return[has[a],i]
            has[nums[i]]=i     