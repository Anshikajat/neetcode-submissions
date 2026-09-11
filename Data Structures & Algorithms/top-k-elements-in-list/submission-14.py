class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f=[[] for i in range(len(nums)+1)]
        d={}
        for i in nums:
            if(i not in d):
                d[i]=1
            else:
                d[i]+=1
        for n,c in d.items():
            f[c].append(n)
        res=[]
        for j in range(len(f)-1,-1,-1):
            for h in f[j]:
                res.append(h)
                if(len(res)==k):
                    return res    

