#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and not head.next:
            return None
        dummy = ListNode(0, head)
        behind = dummy
        ahead = head
        for _ in range(n):
            ahead = ahead.next
        while ahead:
            behind = behind.next
            ahead = ahead.next
        behind.next = behind.next.next if behind.next else None
        return dummy.next
# @lc code=end

