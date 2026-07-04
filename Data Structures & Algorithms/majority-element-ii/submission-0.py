class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        h={}
        a=[]
        for i in range(0,len(nums)):
            if(nums[i] not in h):
                h[nums[i]]=1
            else:
                h[nums[i]]+=1
        for i in h:
            if(h[i]>n):
                a.append(i)
        return a                    
        