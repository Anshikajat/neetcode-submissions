class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        for i in asteroids:
            while( s and s[-1]>0 and i<0):
                d=i+s[-1]
                if(d>0):
                    i=0
                elif(d<0):
                    s.pop()
                else:
                    i=0
                    s.pop()  
            if(i):
                s.append(i)                    
        return s            

        