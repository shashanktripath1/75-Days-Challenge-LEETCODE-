class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a="abcdefghijklmnopqrstuvwxyz"
        for i in a:
            if i not in sentence:
                return False
        return True