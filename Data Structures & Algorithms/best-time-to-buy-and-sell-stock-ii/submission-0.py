class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=1
        m=0
        while(i<len(prices)):
            if(prices[i-1]<prices[i]):
                m+=prices[i]-prices[i-1]
            i+=1    
        return m
            



        