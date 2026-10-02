class FreqStack:

    def __init__(self):
        self.s={}
        self.c=0
        self.h={}

    def push(self, val: int) -> None:
        vc=1
        if(val in self.h):
            vc=self.h[val]+1
        self.h[val]=vc
        if(vc>self.c):
            self.c=vc
            self.s[vc]=[]
        self.s[vc].append(val)        


    def pop(self) -> int:
        res=self.s[self.c].pop();
        self.h[res]-=1
        if(not self.s[self.c]):
            self.c-=1
        return res    
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()