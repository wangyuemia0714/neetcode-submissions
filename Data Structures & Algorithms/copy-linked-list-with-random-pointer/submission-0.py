"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        copy_map = {}
        
        while curr:
            copy_map[curr] = Node(curr.val) # 复制原链表
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                copy_map[curr].next = copy_map[curr.next]
            if curr.random:
                copy_map[curr].random = copy_map[curr.random]
            curr = curr.next

        return copy_map[head]

        

        





        