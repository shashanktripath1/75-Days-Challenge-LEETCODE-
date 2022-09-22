class Solution:
    def reverseWords(self, s: str) -> str:
        split=s.split(' ')
        split=[i[::-1] for i in split]
        return ' '.join(split)