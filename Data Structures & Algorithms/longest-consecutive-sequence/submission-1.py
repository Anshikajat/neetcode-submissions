class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        p=set(nums)

    
        a=[]
        s=0
        for i in p:
            a=[]
            if(i-1 not in p):
                a.append(i)
                c=0
                while a[c]+1 in p:
                    a.append(a[c]+1)

                    c=c+1
            if(len(a)>s):
                s=len(a)    
               
            i+=1
        return s  
                