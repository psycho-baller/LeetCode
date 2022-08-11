class Solution:
    def numberOfSteps(self, num: int) -> int:
        def recursion(num,steps):
            if num == 0:
                return steps
            if num % 2 == 0:
                steps += 1
                return recursion(num // 2, steps)
            else:
                steps += 1
                return recursion(num - 1, steps)

        steps = 0
        return recursion(num,steps)
