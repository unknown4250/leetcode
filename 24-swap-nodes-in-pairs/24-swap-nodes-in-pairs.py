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
        
        root = prev = ListNode(head)
        prev.next = head
        
        while head and head.next:
            # 'b' points 'a(head)'
            b = head.next
            head.next = b.next
            b.next = head
            
            # 'prev'(=previous nodes of a) points 'b'
            prev.next = b
            
            # move for the next comparison
            head = head.next
            prev = prev.next.next
        
        # 연결 리스트의 head를 가리키는 노드가 직접 바뀌므로
        # head를 리턴하지 못하고 head의 이전 값인 root의 next를 리턴하게 됨
        return root.next