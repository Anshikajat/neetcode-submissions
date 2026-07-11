class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i=0
        j=len(people)-1
        p=sorted(people)
        c=0
    
        while(i<j):
            
            if(p[i]==limit):
                c=c+1
                i=i+1
                
                continue
            if(p[j]==limit):
                c=c+1
                j=j-1
                
                continue
            if(p[i]+p[j]==limit):
                c=c+1
                i=i+1
                j=j-1
                
                continue
            if(p[i]+p[j]>limit):
                j=j-1
                c=c+1
                
                
            else:
                c=c+1
                i=i+1
                j=j-1
                
        if(i==j):
            c=c+1        
               
        return c        







        