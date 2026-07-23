class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        # an=set()
        
        
        # for i in nums:
        #     if(i in an):
                
        #         return True
        #     an.add(i)
            
            
            
        
        # return False
        an=set()
        for i in nums:
            if i in an:
                return True
            else:
                an.add(i)
        return False            


                