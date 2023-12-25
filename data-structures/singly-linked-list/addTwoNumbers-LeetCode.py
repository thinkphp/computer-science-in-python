# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        head = l1
        l1_prev = None
        while l1 and l2:
            raw_val = carry_over + l1.val + l2.val
            # What digit goes in node
            l1.val = raw_val % 10
            # What carries over
            carry_over = raw_val // 10
            # Increment prev
            l1_prev = l1
            # Incerement pointers
            l1 = l1.next
            l2 = l2.next

        # If l1 ran out BEFORE l2
        if l2:
            l1_prev.next = l2
            l1 = l2

        # We now may have more l1, then continue carryover process
        while l1:
            raw_val = carry_over + l1.val
            # What digit goes in node
            l1.val = raw_val % 10
            # What carries over
            carry_over = raw_val // 10
            # Incerement pointers
            l1_prev = l1
            l1 = l1.next
        if carry_over > 0:
            l1_prev.next = ListNode(val = carry_over)
        return head
