class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        p=[]
        
        for i in nums:
            if(i not in h):
                h[i]=1
            else:
                h[i]=h[i]+1
        e=sorted(h.values(),reverse=True)
        c=0
                
        for i in range(0,len(h)):
            for key, value in h.items():
                if(len(p)<k and value==e[c]):
            
                    p.append(key)
                    c=c+1
                if(c>len(e)):
                    break    
                    
        return p            

                



