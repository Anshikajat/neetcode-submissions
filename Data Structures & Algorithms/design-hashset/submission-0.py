class MyHashSet:

    def __init__(self):
    
       self.p=[]
       for i in range(0,1000):
        self.p.append([])


    def add(self, key: int) -> None:
        k=key%1000
        if(key not in self.p[k]):
           
            self.p[k].append(key)

        

    def remove(self, key: int) -> None:
        k=key%1000
        if key in self.p[k]:
            self.p[k].remove(key)

        

    def contains(self, key: int) -> bool:
        k=key%1000
        if key in self.p[k]:
            return True
        else:
            return False    
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)