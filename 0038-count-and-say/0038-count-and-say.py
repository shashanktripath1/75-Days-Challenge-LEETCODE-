class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        previous=self.countAndSay(n-1)
        count=1
        answer=""
        for i in range(len(previous)):
            if i==len(previous)-1 or previous[i]!=previous[i+1]:
                answer+=str(count)+previous[i]
                count=1
            else:
                count+=1
        return answer