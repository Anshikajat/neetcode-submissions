class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        an=set()
        
        
        for i in nums:
            if(i in an):
                
                return True
            an.add(i)
            
            
            
        
        return False


                