class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList or endWord not in wordList:
            return []
        
		# 1. Construct a star mapping. e.g. '*og' -> ['dog', 'log']
        starMapping = defaultdict(list)
        # Add beginword to list. So the list contains all the words
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                starWord = word[:i] + '*' + word[i + 1:]
                starMapping[starWord].append(word)
        
		# 2. Use the star mapping to contruct a graph mapping. e.g. 'hot' -> ['dot', 'lot'], 'dot' -> ['hot', 'lot']
        graph = defaultdict(list)
        for starWord, words in starMapping.items():
            if len(words) > 1:
                for i in range(len(words)):
                    graph[words[i]] = graph[words[i]] + words[:i] + words[i + 1:]
                    
		# 3. Use BFS. Stop once found the endWord. Store each level of the graph into levels. Similar to "Tree Level Traverse". Note that don't put the level of the endWord in the levels
        queue = deque([beginWord])
        visited = set([beginWord])
        found = False
        levels = []
        
        while queue and not found:
            queueSize = len(queue)
            row = set()
            for i in range(queueSize):
                node = queue.popleft()
                row.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                    # Check the endWord in neighbor value to avoid traverse the level of the endWord
                    if neighbor == endWord:
                        found = True
            levels.append(row)
        
		# 4. Construct the result. Steps here is 
		#  a) Reverse the levels. So levels would be [[dog, log], [dot, lot], [hot], [hit]]
		#  b) Construct the result from end to beginning. We need to loop for len(levels) time. And in each loop, we need to check the corresponding level.
        result = [[endWord]]
        levels.reverse()
        for i in range(len(levels)):
            backPathNum = len(result)
            for j in range(backPathNum):
                backPath = result.pop(0)
                head = backPath[0]
                for node in levels[i]:
                    if node in graph[head]:
                        newPath = copy.deepcopy(backPath)
                        newPath.insert(0, node)
                        result.append(newPath)
                        
        return result