"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional

from desing_linked_list import LinkedList


class Solution:
    def mergeTwoLists(self, list1: Optional[LinkedList], list2: Optional[LinkedList]) -> Optional[LinkedList]:
        dummy = LinkedList()
        tail = dummy

        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next



'''
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

'''

L1 = LinkedList()
L1.add_end(1)
L1.add_end(2)
L1.add_end(3)
L1.add_end(4)
L2 = LinkedList()
L2.add_end(10)
L2.add_end(20)
L2.add_end(30)
L2.add_end(40)
print(Solution().mergeTwoLists(L1, L2)) # 4 -> 3 -> 2 -> 1 