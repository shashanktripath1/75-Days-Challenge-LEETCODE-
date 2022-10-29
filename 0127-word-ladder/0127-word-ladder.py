class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s=set(wordList)
        l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z']
        queue=deque([])
        queue.append([beginWord,0])
        while queue:
            a,b=queue.popleft()
            if a==endWord:
                return b+1
            for j in range(len(a)):
                for i in l:
                    if (a[:j]+i+a[j+1:]) in s and (a[:j]+i+a[j+1:])!=beginWord:
                        s.remove(a[:j]+i+a[j+1:])
                        queue.append([a[:j]+i+a[j+1:],b+1])
        return 0
        
        # sw,tw,wl=beginWord,endWord,wordList
        # s=set(wl)
        # l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
        # 'u','v','w','x','y','z']
        # q=deque([])
        # q.append([sw,0])
        # while q:
        #     a,b=q.popleft()
        #     if a == tw:
        #         return b+1
        #     for j in range(len(a)):
        #         for i in l:
        #             if (a[:j]+i+a[j+1:]) in s and (a[:j]+i+a[j+1:])!=sw:
        #                 s.remove(a[:j]+i+a[j+1:])
        #                 q.append([a[:j]+i+a[j+1:],b+1])
        # return 0