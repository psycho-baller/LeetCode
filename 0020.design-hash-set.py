# https://leetcode.com/problems/design-hashset/description/
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#
# @lc code=start
from math import floor


class MyHashSet:
    def eval_hash(self, key):
        return floor(self.hashset_len * (key*self.k % 1))


    def __init__(self):
        self.hashset_len = 1000
        self.k = 0.2879
        self.hashset = [[] for _ in range(self.hashset_len)]

    def add(self, key: int) -> None:
        index = self.eval_hash(key)
        if key not in self.hashset[index]:
            self.hashset[index].append(key)

    def remove(self, key: int) -> None:
        index = self.eval_hash(key)
        if key in self.hashset[index]:
            self.hashset[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.eval_hash(key)
        return key in self.hashset[index]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
