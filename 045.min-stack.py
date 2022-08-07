#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self, data=[]):
        self.data = data
        self.mini = []

    def push(self, val: int) -> None:
        self.mini.append(min(val, self.mini[-1])) if self.mini else self.mini.append(val)
        self.data.append(val)

    def pop(self) -> None:
        self.data.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mini[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

