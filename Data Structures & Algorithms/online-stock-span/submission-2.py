class StockSpanner:

    def __init__(self):
        self.s=[]

    def next(self, price: int) -> int:
        i=-1
        a=1
        while(self.s and self.s[i][1]<=price):
            a+=self.s[i][0]
            i=len(self.s)-a
            if(i<0):
                break
        self.s.append((a,price)) 
        return a   
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)