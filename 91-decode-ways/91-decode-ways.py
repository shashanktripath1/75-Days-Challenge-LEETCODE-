class Solution:
    def numDecodings(self, s: str) -> int: 
        dp = [-1 for i in range(len(s)+1)]
        def f(i):
            if(i<0):
                return 1
            if(i==0):
                take_one=0
                if(s[0]=="0"):
                    return 0
                else:
                    return 1
            if(dp[i]!=-1):
                return dp[i]
            else:
                takeone=0
                taketwo=0
                str1=s[i-1:i+1]
                str2=s[i:i+1]
				#Checking if the str1 contains 0 at first position and checking if str1 is less than equals 26 or not
                if(str1[0]=="0" or int(str1)>26):
                    taketwo=0
                else:
                    taketwo=f(i-2)
				#Similarly checking for the other string containing only one element.
                if(str2[0]=="0" or int(str2)>26):
                    takeone=0
                else:
                    takeone=f(i-1)
                dp[i] = takeone+taketwo
                return dp[i]
        return f(len(s)-1)
        