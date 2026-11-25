class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=[0 for i in range(26)]
        b=[0 for i in range(26)]
        l=0
        for i in range(len(s1)):
            j=ord(s1[i])-97
            a[j]+=1
        for i in range(len(s2)):
            j=ord(s2[i])-97
            b[j]+=1
            if(i-l+1>=len(s1)):
            
                print("b",b)  
                print(l,i) 
                if(a==b):
                    return True
                else:
                    j=ord(s2[l])-97
                    b[j]-=1
                    l+=1
                   
        return False
        