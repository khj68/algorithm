class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        prev = None
        
        if not head.next:
            return True
        
        while fast and fast.next:
            fast = fast.next.next
            prev, prev.next, slow = slow, prev, slow.next
            
        if fast:
            slow = slow.next
        
        while prev and prev.val == slow.val:
            slow = slow.next
            prev = prev.next
        
        return not prev
        
            


head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(1)
print(isPalindrome(0, head))