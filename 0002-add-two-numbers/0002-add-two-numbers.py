# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        leading = ListNode()

        e1 = l1
        e2 = l2
        beforeNode = leading
        next = 0
        while e1 is not None or e2 is not None or next != 0:
            v1 = 0
            v2 = 0
            if e1 is not None:
                v1 = e1.val
                e1 = e1.next
            if e2 is not None:
                v2 = e2.val
                e2 = e2.next

            node = ListNode((v1 + v2 + next) % 10, None)
            beforeNode.next = node
            beforeNode = node

            next = (v1 + v2 + next) // 10
        
        return leading.next