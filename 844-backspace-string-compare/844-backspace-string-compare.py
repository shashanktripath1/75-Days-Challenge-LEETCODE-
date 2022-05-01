class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1,stack2=[],[]
        for i in s:
            if i!='#':
                stack1.append(i)
            elif stack1:
                stack1.pop()
        for i in t:
            if i!='#':
                stack2.append(i)
            elif stack2:
                stack2.pop()
        return stack1==stack2
        