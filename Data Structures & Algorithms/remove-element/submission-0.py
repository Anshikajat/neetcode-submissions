class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s=0
        c=0
        for i in range(0,len(nums)):
            if(nums[i]!=val):
                nums[c]=nums[i]
                c=c+1
        
            else:
                s=s+1
                
        for i in range(len(nums)-s,len(nums)):
            nums[i]="_"
        return len(nums)-s    
                        
        