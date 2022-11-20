class Solution:
    def update(self, sign, num, stack):
        if sign == "+":
            stack.append(num)
        if sign == "-":
            stack.append(-num)
        return stack

    def solve(self, i, s):
        stack, num, sign = [], 0, "+"
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "+" or s[i] == "-":
                stack = self.update(sign, num, stack)
                num, sign = 0, s[i]
            elif s[i] == "(":
                num, i = self.solve(i + 1, s)
            elif s[i] == ")":
                stack = self.update(sign, num, stack)
                return sum(stack), i
            i += 1
        # print(num, sign)
        stack = self.update(sign, num, stack)
        return sum(stack)

    def calculate(self, s: str) -> int:
        return self.solve(0, s)