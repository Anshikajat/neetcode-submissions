class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=len(nums)
        h={}
        while(i<j):
            if(nums[i] not in h):
                h[nums[i]]=[i]
            else:
                h[nums[i]].append(i)    
            i=i+1
        print(h)    
            
        for i,j in h.items():
            if(len(j)>1):
                p=0
                while(p<len(j)-1):
                    if(abs(j[p] - j[p+1]) <= k):
                        return True
                    p=p+1
        return False                

                

        