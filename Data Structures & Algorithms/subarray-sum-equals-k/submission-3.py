class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        pre={0:1}
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if((sum-k) in pre):
                c+=pre[sum-k]
            if(sum not in pre):
                pre[sum]=1
            else:
                pre[sum]+=1    
            
            
                       
            
        return c            



        