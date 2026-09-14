class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h={}
        a=[]
        for i in nums:
            if(i not in h):
                h[i]=1
            else:
                h[i]+=1
        for i,j in h.items():
            if(h[i]>(len(nums))/3):
                a.append(i)
        return a                    


        