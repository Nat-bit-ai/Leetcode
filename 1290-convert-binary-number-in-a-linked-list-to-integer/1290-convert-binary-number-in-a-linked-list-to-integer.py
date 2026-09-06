# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        cur = head
        new = head
        i = 0
        num = 0
        while cur:
            cur = cur.next
            i += 1
        while new:
            num += new.val * 2**(i-1)
            new = new.next
            i -= 1
        return num

