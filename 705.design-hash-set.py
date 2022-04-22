# https://leetcode.com/problems/design-hashset/description/
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#
# @lc code=start
class MyHashSet:

    def __init__(self):
        self.hashset = set()
        self.output = []
        self.output.append(self.hashset)

    def add(self, key: int) -> None:
        self.output.append(self.hashset.add(key))

    def remove(self, key: int) -> None:
        self.output.append(self.hashset.remove(key))

    def contains(self, key: int) -> bool:
        self.output.append(self.hashset.__contains__(key))
        return self.output[-1]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
