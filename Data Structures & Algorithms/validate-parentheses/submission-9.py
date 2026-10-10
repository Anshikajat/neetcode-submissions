class Solution:
    def isValid(self, s: str) -> bool:
       
        i=0
        st=[]
        while(i<len(s)):
            if(s[i]=="(" or s[i]=="{" or s[i]=="["):
                st.append(s[i])
            elif(s[i]==")"):
                if(not st or st.pop()!="("):
                   return False
            elif( s[i]=="]"):
                if(not st or st.pop()!="["):
                   return False
            elif(s[i]=="}"):
                if(not st or st.pop()!="{"):
                   return False
                  

                                
            i+=1
        if(len(st)==0):    
           return True  
        return False         
        