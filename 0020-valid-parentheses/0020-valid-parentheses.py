class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                ch=stack[-1]
                stack.pop()
                if (i==')' and ch=='(') or (i==']' and ch=='[') or (i=='}' and ch=='{'):
                    continue
                return False
        return len(stack)==0