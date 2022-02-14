# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        while head:
            if head.val == None:
                return True
            if head.next:
                head.val = None
                head = head.next
            else:
                return False
