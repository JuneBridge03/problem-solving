# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return True
        
        s_straight = ""
        s_back = ""

        while head != None:
            s_straight += str(head.val)
            s_back = str(head.val) + s_back
            head = head.next

        return s_straight == s_back