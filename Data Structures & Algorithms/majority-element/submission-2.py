class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=1
        a=nums[0]
        for i in range(1,len(nums)):
            if(nums[i]==a):
                c+=1
            if(nums[i]!=a and c!=0):
                c-=1
            if(c==0):
                a=nums[i]
        return a                


        
                              
        
            

            
                      
          


        