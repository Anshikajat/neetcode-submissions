class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h={}
        for i in range(0,len(nums)):
            if(nums[i] not in h):
                h[nums[i]]=[i]
            else:
                j=0
                while(j<len(h[nums[i]])):
                    if(i-h[nums[i]][j]<=k):
                        return True
                    j+=1
                h[nums[i]].append(i)        
                    
        return False            



        