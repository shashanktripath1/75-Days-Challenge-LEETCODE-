class Solution:
    def minOperations(self, s: str) -> int:
        x,y=0,0
        for i in range(len(s)):
            if i%2==0 and s[i]=='1':
                x+=1
            elif i%2==1 and s[i]=='0':
                x+=1
            elif i%2==0 and s[i]=='0':
                y+=1
            elif i%2==1 and s[i]=='1':
                y+=1
        return min(x,y)

                
 