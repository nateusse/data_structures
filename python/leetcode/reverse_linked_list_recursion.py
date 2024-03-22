"""
Given the head of a singly linked list, 
reverse the list, and return the reversed list.
USE RECURSION
"""



from typing import Self
from python.leetcode.design_linked_list_prenode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #base case
        if not head: #si no hay head 
            return None #nada que devolver
        

        newHead = head #mantener head, inicialmente es head
        if head.next: #si hay un next
            newHead = self.reverseList(head.next) #pasar el siguiente
            head.next.next = head #reversar link entre next y head
        
        head.next = None #cortar el link entre head y next
        return newHead
