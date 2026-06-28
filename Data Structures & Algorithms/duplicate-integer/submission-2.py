class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        an=set()
        
        i=0
        j=len(nums)
        while(i<j):
            if(nums[i] in an):
                
                return True
            an.add(nums[i])
            
            
            i=i+1
        
        return False


                