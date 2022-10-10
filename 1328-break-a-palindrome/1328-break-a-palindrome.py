class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        if n==1:
            return ""
        s=""
        for i in range(n):
            if palindrome[i]!='a':
                s+='a'
                s+=palindrome[i+1:]
                if s!=s[::-1]:
                    return s
                else:
                    break
            s+=palindrome[i]
        return palindrome[:-1]+'b'