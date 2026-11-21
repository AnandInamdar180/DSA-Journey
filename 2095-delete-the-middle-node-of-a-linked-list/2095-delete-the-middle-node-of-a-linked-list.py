# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head.next is None:
            return None
        current = head
        count = 0

        while current:
            count += 1
            current = current.next
        mid = count // 2
        current = head
        previous = None
        for i in range(mid):
            previous = current
            current = current.next
        previous.next = current.next
        return head