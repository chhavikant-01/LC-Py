# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # Step 1: Find the middle of the list using fast/slow pointers
        # This efficiently splits our list in half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        # This allows us to traverse from middle to end backwards
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Find maximum twin sum by comparing nodes from
        # start and reversed second half
        max_sum = 0
        first = head
        second = prev  # prev is now the head of reversed second half
        
        # We only need to go until the middle (where second becomes None)
        while second:
            # Calculate twin sum and update maximum if necessary
            twin_sum = first.val + second.val
            max_sum = max(max_sum, twin_sum)
            
            # Move to next pairs
            first = first.next
            second = second.next
        
        return max_sum

        
