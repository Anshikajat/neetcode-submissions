class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # p=len(nums)/2
        # can=nums[0]
        # c=1
        
        # for i in nums:
        #     if(c==0):
                
        #         can=i
                
        #     if(i==can):
        #         c=c+1
        #     else:
        #         c=c-1 
        # return can

        res=nums[0]
        c=1
        for i in nums:
            if(c==0):
                res=i
            if(i==res):
                c+=1
            if(i!=res):
                c=c-1
            
        return res                

        
                              
        
            

            
                      
          


        