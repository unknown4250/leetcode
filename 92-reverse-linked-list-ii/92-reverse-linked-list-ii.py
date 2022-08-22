# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        
        if not head or left == right:
            return head
        
        root = start = ListNode(None)
        root.next = head
        
        # start의 위치(root 다음)는 고정
        # start와 end의 값 고정됨
        for _ in range(left-1):
            start = start.next
        end = start.next
        
        for _ in range(right-left):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
            
        return root.next