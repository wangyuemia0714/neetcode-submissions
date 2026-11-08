# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # after the while loop, slow points to the last element
        # of the first half, slow.next is the start of second half
        # fast is either the last element or NULL

        # reverse the second half 
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # prev is the head node of the reversed second half
        
        # merge two list

        
        first = head
        while prev:
            temp1 = first.next
            temp2 = prev.next
            first.next = prev
            prev.next = temp1
            prev = temp2
            first = temp1


      







      
