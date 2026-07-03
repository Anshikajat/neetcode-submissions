class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pr=[]
        s=1
        an=[]
        pr.append(1)
        su = [0] * len(nums)
        su[len(nums)-1]=1
        for n in range(1,len(nums)):
            s=s*(nums[n-1])
            pr.append(s)
        s=1
        for n in range(len(nums)-1,0,-1):
            s=s*nums[n]
            su[n-1]=s


                
                
        for i in range(0,len(nums)):
            an.append(su[i]*pr[i])
        return an       

                    

        