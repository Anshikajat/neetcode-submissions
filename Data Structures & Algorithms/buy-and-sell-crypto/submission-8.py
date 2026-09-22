class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        i=0
        j=len(prices)-1
        s=i
        while(i<j):
            if(prices[i]<prices[s]):
                s=i
            a=prices[i+1]-prices[s]    
            if(a>m):
                m=a
            i+=1
        return m            
        