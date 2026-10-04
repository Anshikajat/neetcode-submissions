class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      i=0
      r=1
      m=0
      while(r<len(prices)):
        if(prices[i]<prices[r]):
            p=prices[r]-prices[i]
            if(p>m):
                m=p
        else:
            i=r
        r+=1            
      return m