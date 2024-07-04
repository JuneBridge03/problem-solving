# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        last = None
        answer = None

        while list1 != None or list2 != None:
            v = 0
            if list2 == None or (list1 != None and list1.val <= list2.val):
                v = list1.val
                list1 = list1.next
            else:
                v = list2.val
                list2 = list2.next
            
            newNode = ListNode(v, None)

            if last != None:
                last.next = newNode
            else:
                answer = newNode
            
            last = newNode
        
        return answer