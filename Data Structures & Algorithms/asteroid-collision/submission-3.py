class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        for i in asteroids:
        

            while(s and s[-1]>0 and i<0):
                if(s[-1]<abs(i)):
                    s.pop()
                    continue
                elif(s[-1]==abs(i)):
                    s.pop()
                    break
                else:
                    break
            else:
                s.append(i)                 
            
        return s               

            
        