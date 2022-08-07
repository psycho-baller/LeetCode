#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        curr = output
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            summ = l1_val + l2_val
            if summ + carry >= 10:
                summ -= 10
                curr.val += summ
                # Carries a one from the previous addition
                carry = 1
            else:
                curr.val += summ
                carry = 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2 or carry:
                curr.next = ListNode(carry)
                curr = curr.next
        return output
# @lc code=end

