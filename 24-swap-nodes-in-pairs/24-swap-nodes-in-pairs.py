# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            
            return p
        
        return head