class Solution:
    def reverseVowels(self, s: str) -> str:
        n=len(s)
        left,right=0,n-1
        ans=list(s)
        vowels="AEIOUaeiou"
        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left <right and s[right] not in vowels:
                right-=1
            ans[left],ans[right]=ans[right],ans[left]
            left+=1
            right-=1
        return "".join(ans)