from collections import deque
from typing import List

class Solution:
    def  ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Creating a queue ds of type {word, transitions to reach ‘word’}.
        q = deque([(beginWord, 1)])

        # Push all values of wordList into a set
        # to make deletion from it easier and in less time complexity.
        word_set = set(wordList)
        word_set.discard(beginWord)

        while q:
            word, steps = q.popleft()

            # Return the steps as soon as the first occurrence of endWord is found.
            if word == endWord:
                return steps

            # Replace each character of word with char from a-z then check if it exists in wordList.
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i+1:]
                    # Check if it exists in the set and push it into the queue.
                    if new_word in word_set:
                        word_set.discard(new_word)
                        q.append((new_word, steps + 1))

        # If there is no transformation sequence possible
        return 0

