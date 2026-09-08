class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       res=""
       for i in range(len(strs[0])):
            f=True
            for j in range(1,len(strs)):
                if(i>=len(strs[j])):
                    f=False
                    break
                if(strs[0][i]!=strs[j][i]):
                    f=False
                    break
            if(f):
             res=res+strs[0][i]
            else:
                break 

       return res            
