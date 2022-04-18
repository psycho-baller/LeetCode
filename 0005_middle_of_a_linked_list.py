from collections import defaultdict
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # gives us the ability to add keys to the dict without initializing it
        dict = defaultdict(int)

        for i in range(len(mat)):
            dict[i] = mat[i].count(1)
        new_dict = defaultdict(int)
        done = False
        while not done:
            for key, value in list(dict.items()):
                if value == min(dict.values()):
                    new_dict[key] = dict.pop(key)
                    break
                    # after removing a pair from the dict,
                    # we re-run the for loop until we get the kth smallest value,
                    # then we can end the while loop
            if len(new_dict) == k:
                done = True
        return list(new_dict.keys())

# print(Solution().kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))