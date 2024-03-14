class Solution:
    #for comments check previous submission of this code
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue=deque()
        queue.append((beginWord,1))
        word_set=set(wordList)
        if beginWord in word_set:
            word_set.remove(beginWord)
        while queue:
            word,steps=queue.popleft()
            if word==endWord:
                return steps
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word=word[:i]+ch+word[i+1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word,steps+1))
        return 0