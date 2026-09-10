class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        
        for i in range(len(strs)):
            p="".join(sorted(strs[i]))
                     
            if(p not in res):
                res[p]=[strs[i]]
            else:
                res[p].append(strs[i])

        return list(res.values())                      


                
