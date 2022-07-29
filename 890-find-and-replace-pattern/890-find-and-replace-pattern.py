class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def find_pattern(word):
            seen,output={},[]
            for char in word:
                if char not in seen:
                    seen[char]=len(seen)
                output.append(seen[char])
            return output
        return [word for word in words if find_pattern(word)==find_pattern(pattern)]