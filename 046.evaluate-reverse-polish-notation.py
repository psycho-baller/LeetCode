#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == "*":
                stack.append(stack.pop() * stack.pop())
            elif val == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            elif val == "+":
                stack.append(stack.pop() + stack.pop())
            elif val == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            else:
                stack.append(int(val))
        return stack[0]
# @lc code=end

