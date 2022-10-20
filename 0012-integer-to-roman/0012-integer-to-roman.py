class Solution:
    def intToRoman(self, num: int) -> str:
        list_roman=[["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        ans=""
        for symbol,number in reversed(list_roman):
            if num//number:
                counter=num//number
                ans+=(symbol*counter)
                num=num%number
        return ans
            