class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        
        s=""
        while(i<len(word1) and i<len(word2)):
            s+=word1[i]+word2[i]
            i=i+1
        if(len(word2)>len(word1)):
            s+=word2[i:len(word2)] 
        else:
               s+=word1[i:len(word1)]
        return s              
            

        