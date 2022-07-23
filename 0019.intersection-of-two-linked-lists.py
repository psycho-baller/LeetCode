#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        def length(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count


        lenA = length(headA)
        lenB = length(headB)
        if lenA < lenB:
            headA, headB = headB, headA
            lenA,lenB = lenB,lenA

        for _ in range(lenA - lenB):
            headA = headA.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
    # @lc code=end
