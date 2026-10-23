class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        res=r
        def cansplit(lar):
            subarray=0
            subcount=0
            for i in nums:
                subcount+=i
                if(subcount>lar):
                    subarray+=1
                    subcount=i
            return subarray+1<=k        

        while l<=r:
            mid=(l+r)//2
            if(cansplit(mid)):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res            

        