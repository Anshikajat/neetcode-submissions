class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # i=0
        # has={}
        # while(i<len(nums)):
        #     dif=target-nums[i]
        #     if(dif in has):
        #         return [has[dif],i]
        #     else:
        #         has[nums[i]]=i
        #     i=i+1 
        an={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if(diff in an):
                return [an[diff],i]
            else:
                an[nums[i]]=i    
            
            
            
                   
        