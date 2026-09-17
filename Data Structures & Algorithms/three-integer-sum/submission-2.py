class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = []
        i = 0
        nums.sort()
        while i < len(nums)-2:
            if(i>0 and nums[i]==nums[i-1]):
                i+=1
                continue
            r = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == r:
                    a.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[k]==nums[k+1]):
                        k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1    
                elif(nums[j] + nums[k] > r):
                    k-=1
                else:
                    j+=1
            i+=1        
        return a                    
