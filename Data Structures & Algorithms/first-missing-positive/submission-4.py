class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        t=len(nums)
        h=set(nums)
        for i in range(1,t+2):
            if(i not in h):
                return i
        