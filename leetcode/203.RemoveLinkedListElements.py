# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # # 더미 노드를 추가하여 edge case를 처리
        # dummy = ListNode(next=head)
        # current = dummy
        
        # # 리스트를 순회하면서 val 값을 가진 노드를 제거
        # while current.next:
        #     if current.next.val == val:
        #         current.next = current.next.next
        #     else:
        #         current = current.next
        
        # # 더미 노드의 다음 노드를 반환
        # return dummy.next

        dummy = ListNode(next=head)
        prev, current = dummy, head

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy.next