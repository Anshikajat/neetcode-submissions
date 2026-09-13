class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre=[1]
        p=1
        res=[]
        for i in nums:
            p*=i
            pre.append(p)
        suf=[1 for i in range(len(nums)+1)]
        s=1
        for i in range(len(nums)-1,-1,-1):
            s*=nums[i]
            suf[i]=s
        for i in range(1,len(nums)+1):
            res.append(pre[i-1]*suf[i])
        return res    

            
        

                    

        