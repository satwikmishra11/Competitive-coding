class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Initialize two pointers
        first = head
        second = head
        
        # Move the first pointer n steps ahead
        for _ in range(n):
            first = first.next
        
        # If the first pointer is None, it means we need to remove the head
        if first is None:
            return head.next
        
        # Move both pointers until the first pointer reaches the end
        while first.next is not None:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        return head
