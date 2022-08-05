#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        # """
        temp_head = head
        fast = head.next
        while fast and fast.next:
            temp_head = temp_head.next
            fast = fast.next.next
        second = temp_head.next
        temp_head.next = None
        prev = None
        while second:
            curr = second
            second = second.next
            curr.next = prev
            prev = curr
        second = prev
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2
# @lc code=end

