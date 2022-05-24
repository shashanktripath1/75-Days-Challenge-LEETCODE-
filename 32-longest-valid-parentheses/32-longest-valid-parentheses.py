class Solution:
	def longestValidParentheses(self, s: str) -> int:

		stack = []

		result = 0

		for i in range(len(s)):

			if s[i] == '(' :
				stack.append(i)
			else:

				if len(stack) != 0:
					if s[stack[-1]] == '(' and s[i] ==')':
						stack.pop(-1)
					else:
						stack.append(i)
				else:
					stack.append(i)

		if len(s) != 0 and len(stack) != 0:

			result = max(result, stack[0])
			result = max(result, len(s)-1 - stack[-1])

			for i in range(len(stack)-1):

				result = max(result, stack[i+1] - stack[i] -1)

			return result

		else:
			result = max(result, len(s))
			return result