class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
	    sw,tw,wl=startWord,targetWord,wordList

		s=set(wl)
        l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z']
        q=deque([])
        q.append([sw,0])
        while q:
            a,b=q.popleft()
            if a == tw:
                return b+1
            for j in range(len(a)):
                for i in l:
                    if (a[:j]+i+a[j+1:]) in s and (a[:j]+i+a[j+1:])!=sw:
                        s.remove(a[:j]+i+a[j+1:])
                        q.append([a[:j]+i+a[j+1:],b+1])
        return 0#Code here


#{ 
 # Driver Code Starts
from collections import deque 
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n = int(input())
		wordList = []
		for i in range(n):
			wordList.append(input().strip())
		startWord = input().strip()
		targetWord = input().strip()
		obj = Solution()
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends