# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has only one node
        # return as is since no reversal needed
        if not head or not head.next:
            return head
        
        # Initialize three pointers:
        # prev: tracks the previous node (starts as None since nothing before first node)
        # curr: tracks the current node we're processing
        # next_node: keeps track of the next node before we change current's pointer
        prev = None
        curr = head
        
        while curr:
            # Save the next node before we modify current's pointer
            next_node = curr.next
            
            # Reverse the pointer of current node to point to previous node
            curr.next = prev
            
            # Move prev and curr one step forward for next iteration
            prev = curr
            curr = next_node
        
        # prev is now pointing to the last node of original list
        # which is our new head
        return prev
        
