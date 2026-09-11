class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        a=[]
        for i in nums:

            if(i not in  d):
                d[i]=1
            else:
                d[i]+=1
        r = sorted(d.items(), key=lambda x: x[1],reverse=True)
        for j in r:
            if(len(a)<k):
                a.append(j[0])
        return a                                
                