class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c=""
        for i in range(0,len(strs[0])):

            s=0
            for j in range(1,len(strs)):
                if((len(strs[j])-1<i)):
                    s=1
                    break
                else:
                    if(strs[0][i]!=strs[j][i]):
                        s=1
                        break
            if(s==0):        
                c=c+strs[0][i]  
            else:
                break          
        return c           
                



        