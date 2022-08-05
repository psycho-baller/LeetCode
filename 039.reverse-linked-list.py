#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            # curr is just being used as a temp pointer each iteration
            curr = head
            head = head.next
            # reverse
            curr.next = prev
            # Advance
            prev = curr
        return prev
        # Noob answer:
        # node = head
        # if not node:
        #     return None
        # stack = []
        # while node:
        #     stack.append(node)
        #     node = node.next
        # reverse_node = stack.pop()
        # pointer = reverse_node
        # while stack != []:
        #     pointer.next = stack.pop()
        #     pointer = pointer.next
        # return pointer
            
# @lc code=end

