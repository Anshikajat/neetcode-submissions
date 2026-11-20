class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a=[]
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            l=i+1
            j=len(nums)-1
            while(l<j):
                t=nums[i]+nums[j]+nums[l]
                if(t==0):
                    a.append([nums[i],nums[j],nums[l]])
                    l+=1
                    j-=1
                    while nums[l] == nums[l - 1] and l < j:
                        l += 1
                elif(t>0):
                    j-=1
                else:
                    l+=1
        return a                    


        