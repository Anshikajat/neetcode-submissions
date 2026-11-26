class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        c=0
        while(j<len(prices)):
            if(prices[j]-prices[i]>c):
                c=prices[j]-prices[i]
            if(prices[j]<prices[i]):
                i=j
            j+=1         
        return c            


        