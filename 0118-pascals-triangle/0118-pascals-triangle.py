class Solution:
    def generate_row(self,row):
        ans=1
        ans_row=[1]
        for col in range(1,row):
            ans*=row-col
            ans//=col
            ans_row.append(ans)
        return ans_row
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for row in range(1,numRows+1):
            ans.append(self.generate_row(row))
        return ans