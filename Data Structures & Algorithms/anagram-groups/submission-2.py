class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # groups = {}

        # for word in strs:
        #     key = "".join(sorted(word))

        #     if key in groups:
        #         groups[key].append(word)
        #     else:
        #         groups[key] = [word]

        # return list(groups.values())
        h={}
        
        for i in strs:
            p="".join(sorted(i))
            if(p not in h):
                h[p]=[i]
            else:
                h[p].append(i)
        
        return list(h.values())              