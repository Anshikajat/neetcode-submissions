class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        an=[]
        n=len(nums)
        for i in range(0,2*n):
            an.append(nums[i-n])
        return an    
        