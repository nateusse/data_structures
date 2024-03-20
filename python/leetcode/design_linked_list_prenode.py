"""

Design Singly Linked List CON NODO dummy, 1 por defecto

Your LinkedList class should support the following operations:
    LinkedList() will initialize an empty linked list.
    int getNode(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
    void insertHead(int val) will insert a node with val at the head of the list.
    void insertTail(int val) will insert a node with val at the tail of the list.
    int remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false,
    otherwise return true.
    int[] getValues() return an array of all the values in the linked list, ordered from head to tail.



"""

# Singly Linked List Node
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # dummy valor para evitar edge cases
        self.head = ListNode(-1)
        #tail is head, solo hay 1 nodo
        self.tail = self.head
    
    def get(self, index: int) -> int:
        # primer nodo es dummy, saltarlo
        curr = self.head.next
        i = 0 # contador
        #no for para deternerse al next None
        while curr:
            if i == index: #si llega al index
                return curr.val #retornar valor
            i += 1 #sumar contador, no infinity loop
            curr = curr.next #saltar al siguiente nodo until None
        return -1  # Index out of bounds or list is empty

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val) #crear nuevo nodo con val
        new_node.next = self.head.next #nuevo nodo referencia al head no dummy
        self.head.next = new_node #head es nuevo nodo
        if not new_node.next:  # If list was empty before insertion
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val) #crear node
        self.tail = self.tail.next #tail es nuevo nodo

    #remover con indice
    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head #empezar cabeza
        while i < index and curr: #mientras no llegue al index y no sea None
            i += 1 #aumentar suma
            curr = curr.next #saltar al siguiente nodo
        
        # Remove the node ahead of curr
        if curr and curr.next: #si hay nodo y hay siguiente
            if curr.next == self.tail: #si el siguiente es tail
                self.tail = curr #tail es el actual
            curr.next = curr.next.next #saltar el siguiente nodo
            return True #removido
        return False #no removido, no existe el index
    
    #con el [] no imprime None
    def getValues(self) -> list[int]:
        curr = self.head.next #empezar en el primer nodo no dummy
        res = [] #lista vacia
        while curr: #mientras no sea None la referencia
            res.append(curr.val) #agregar el valor
            curr = curr.next #saltar al siguiente nodo
        return res #retornar lista
    


LL1 = LinkedList()
LL1.insertHead(44) # 44
LL1.insertHead(22) # 22, 44
LL1.insertTail(66)  # 22, 44, 66
LL1.remove(1) # 22, 66
print(LL1.getValues()) # [22, 66]