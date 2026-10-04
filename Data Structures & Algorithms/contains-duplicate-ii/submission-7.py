class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        a=0
        h=set()
        
        while(i<len(nums)):

            if(len(h)>k):
                h.remove(nums[a])
                a+=1
        
            if(nums[i] not in h):
                h.add(nums[i])
            else:
                return True
             
            i+=1    
        return False                