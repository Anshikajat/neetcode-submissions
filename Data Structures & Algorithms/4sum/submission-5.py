class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        q=[]
        res=[]
        def ksum(k,start,target):
            if(k!=2):
                for i in range(start,len(nums)+1-k):
                    if(i>start and nums[i]==nums[i-1]):
                        continue
                    q.append(nums[i])
                    ksum(k-1,i+1,target-nums[i])
                    q.pop()
                return

            l=start
            j=len(nums)-1
            while(
            l<j):
                if(nums[l]+nums[j]>target):
                    j-=1
                elif(nums[l]+nums[j]<target):
                    l+=1
                else:
                    res.append(q+[nums[l],nums[j]])
                    l+=1
                    while(l<j and nums[l]==nums[l-1]):
                        l+=1
        ksum(4,0,target)
        return res                    


        