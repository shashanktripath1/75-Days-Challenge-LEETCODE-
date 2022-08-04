class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if p == q: 
            return 1
        
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2
            
        if p % 2 == 1 and q % 2 == 0:
            return 0
        elif p % 2 == 1 and q % 2 == 1:
            return 1
        elif p % 2 == 0 and q % 2 == 1:
            return 2
