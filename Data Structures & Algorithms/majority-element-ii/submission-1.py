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
            
            if(len(h)>2):
                hp={}
                for k,v in h.items():
                    if(v>1):
                        hp[k]=v-1
                h=hp 

        for i in h:
            if(nums.count(i) > n):
                a.append(i)
        return a                    
        