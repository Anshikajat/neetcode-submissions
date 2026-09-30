class StockSpanner:

    def __init__(self):
        self.s=[]

    def next(self, price: int) -> int:
        if(self.s==[]):
            self.s.append(price)
            return 1
        i=len(self.s)-1  
        c=1  
        while(i>-1):
            
            if(self.s[i]>price):
                break
            c+=1 
            i-=1
        self.s.append(price)
        return c           
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)