# list solution
# def isPalindrome(head: list) -> bool:
#     for i in range(len(head)//2):
#         if head[i] != head[-i-1]:
#             return False
#     return True
# print(isPalindrome(head=[1,2,1]))

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # create a stack to store the values of the linked list
        stack = []
        # create a variable to store the current node
        current_node = head
        # loop through the linked list
        while current_node:
            # add the current node's value to the stack
            stack.append(current_node.val)
            # move to the next node
            current_node = current_node.next
        # loop through the linked list again
        while head:
            # check if the head's value is the same as the value at the top of the stack
            if head.val != stack.pop():
                # if not, return False
                return False
            # move to the next node
            head = head.next
        # return True if the loop completes
        return True