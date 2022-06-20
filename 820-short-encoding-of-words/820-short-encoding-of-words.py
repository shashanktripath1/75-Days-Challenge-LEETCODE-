class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(w[::-1] for w in words)
        result = 0
        for i, word in enumerate(words):
            if i == len(words) - 1 or not words[i+1].startswith(word):
                result += len(word) + 1
                
        return result