# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(-1)
        cursor = head

        # list1이나 list2가 None이면 while문 종료
        while list1 != None and list2 != None:
            # 값을 비교해서 포인터가 가리킬 다음 노드 선택
            if list1.val < list2.val:
                cursor.next = list1
                list1 = list1.next # 다음 노드를 가리키도록 업데이트
            else:
                cursor.next = list2
                list2 = list2.next
            
            # 포인터를 다음 노드로 옮김
            cursor = cursor.next
        
        # list1이 None이면 포인터는 list2의 나머지를 가리킴
        if list1 == None:
            cursor.next = list2
        # list2가 None이면 포인터는 list1의 나머지를 가리킴
        else:
            cursor.next = list1
        
        return head.next