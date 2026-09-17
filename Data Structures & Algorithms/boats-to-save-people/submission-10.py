class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

    
        c=0
        people.sort()
        i=0
        j=len(people)-1
        while(i<=j):
            if(people[i]+people[j]<=limit):
                c=c+1
                j-=1
                i+=1
            elif(people[j]>=limit):
                c=c+1
                j-=1
            elif(people[i]+people[j]>limit):
                c=c+1
                j-=1
            
            else:
                c+=1
                i+=1
                
        return c                
        