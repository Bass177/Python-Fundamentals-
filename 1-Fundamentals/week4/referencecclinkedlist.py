
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head node Created:", self.head.value)
            return

        node =self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Append new node with value:", node.next.value)

    def preppend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print("Head node Created:", self.head.value)
            return
       
        new_node.next = self.head
        self.head = new_node

        print("Prepended new Head Node with value:", new_node.value)
        print("Node following Head is:", new_node.next.value)
       
   
llist = LinkedList()
llist.preppend("new first node")
llist.preppend("Inserted new First Node")