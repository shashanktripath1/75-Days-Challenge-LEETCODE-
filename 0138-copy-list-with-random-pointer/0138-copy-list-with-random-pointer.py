
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        temp=head
        while temp is not None:
            new_node=Node(temp.val,temp.next)
            temp.next=new_node
            temp=new_node.next
        Iter=head
        while Iter!=None:
            if Iter.random!=None:
                temp=Iter.random
                Iter.next.random = temp.next
            Iter=Iter.next.next
        dummy=Node(0,None)
        Iter=head
        copy=dummy
        while Iter is not None:
            front=Iter.next.next
            copy.next=Iter.next
            Iter.next=front
            copy=copy.next
            Iter=Iter.next
        return dummy.next
        
        