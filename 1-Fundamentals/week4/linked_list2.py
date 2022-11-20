class Node: 
    def __init__(self , value):
        self.value = value
        self.next = None
        #declaration of Node class, with value and next intitialized. value allows for a value to be stored in the node class, next refers to the next node that will be created
def iter_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next
#his while loop traverses the linked list from node to node, printing the value for each then moving on to the next.

head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")
head.next.next.next = Node("4th Node")
iter_linked_list(head)