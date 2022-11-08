# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        # 사이클 여부를 확인하기 위한 두 포인터
        slow = head
        fast = head.next

        while slow != fast:
            # 포인터가 None이거나 None을 가리키게 되면 사이클 X
            if not fast or not fast.next:
                return False

            # 포인터 이동 (slow는 1칸, fast는 2칸)
            slow = slow.next
            fast = fast.next.next

        # 두 포인터가 만나게 되면 사이클 O
        return True
        