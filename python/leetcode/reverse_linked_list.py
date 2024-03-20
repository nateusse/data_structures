"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import Optional

from desing_linked_list import LinkedList


class Solution:
    def reverseList(self, head: Optional[LinkedList]) -> Optional[LinkedList]:
        previus = None
        current = head
        while current:
            next_node = current.next
            current.next = previus
            previus = current
            current = next_node
        return previus




"""
Big o(n) time complexity, momory O(1), pointers no new data str
for recursion seria 0(n) con memoria O(n)

       if not head: return None
       next_node = head
       if head.next:
            next_node = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        reutrn next_node

        1 no se ejecuta, 2 nodos a o mas
"""

LL = LinkedList()
LL.add_begin(1)
LL.add_begin(2)
LL.add_begin(3)
LL.add_begin(4)
print(Solution().reverseList(LL.travers_linked_list())) # 4 -> 3 -> 2 -> 1 