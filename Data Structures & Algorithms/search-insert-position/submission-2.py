class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s=0
        l=len(nums)-1
        while(s<=l):
            m=(s+l)//2
            if(nums[m]==target):
                return m
            elif(nums[m]<target):
                s=m+1
            else:
                l=m-1
        return s                 