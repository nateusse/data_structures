"""
Design Singly Linked List WITHOUT INITIAL NODE

Your LinkedList class should support the following operations:

    LinkedList() will initialize an empty linked list.
    Node sera el auxiliar
    traverser_linked_list() recorre los nodos. Pilas con vacio
    add_beggining(data) pone en head
    add_end(data) pone en tail
    add_after(data, index) pone despues del nodo indicado
    add_before(data, index) pone antes del nodo indicado
    delete_begin(), delete_last() hace justo eso, dahhh
    delete_by_value(value) remueve valor dado
"""


#clase para crear un simple nodo
class Node:
    def __init__(self,data):
        #los nodos tienen data y referencia
        self.data = data
        self.ref = None #no apunta a nada, es 1


#empezar a anidar los nodos
class LinkedList:

    def __init__(self):
        # no hay nodo inicial, sino  seria Node(-1) por ejemplo
        self.head = None #referncia

    def travers_linked_list(self):
        if self.head is None:
            print("Linked list is empty!") #no nodes
        else:
            #empezar por la cabeza, random variable
            n = self.head
            #while apra que pare en tail
            while n is not None:
                print(n.data)
                n = n.ref #saltar siguiente nodo

# add in head 
    def add_begin(self,data):
        new_node = Node(data) #iniciar nodo con data
        new_node.ref = self.head #nuevo nodo referencia a la hcurrent ead
        self.head = new_node #nuew_node es el nuevo head, dejo ir el anterior        


# add in tail
    def add_end(self,data):
        new_node = Node(data) #crear nuevo nodo
        if self.head is None: #si no hay head
            self.head = new_node #nuevo nodo es head
        else:
            n = self.head #empezar por head
            while n.ref is not None: #mientras no llegue a tail
                n = n.ref #saltar al siguiente nodo
            n.ref = new_node #tail es nuevo nodo


#  insertar nodo despues del nodo indicado
    def add_after(self,data, index):
        n = self.head #emepzar por head
        while n is not None: #mientras no sea tail
            if index==n.data: #si el index es igual al nodo
                break
            n = n.ref 
        if n is None:
            print("node is not presesnt in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

#Insertar nodo antes del nodo indicado
    def add_before(self,data,index):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data==index:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==index:
                break
            n = n.ref        
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node    
    
    #delete first node
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        else:
            self.head=self.head.ref

    #delete last node
    def delete_last(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    #delete node by value
    def delete_by_value(self, value):
        if self.head is None:
            print("Linked List is empty can't delete!")
            return
        if value==self.head.data: #if head is the value
            self.head=self.head.ref #head is the next node
            return #end
        n = self.head #start at head
        while n.ref is not None: #while not tail
            if n.ref.data==value: #if the next node is the value
                break #end
            n = n.ref #next node
        if n.ref is None: #if the next node is tail
            print("Node is not present!") #
        else:
            #next node is the next next node,
            n.ref = n.ref.ref #me salto el nodo que quiero borrar, apunto siguiente
            
            

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_end(30)
print(LL1.travers_linked_list())