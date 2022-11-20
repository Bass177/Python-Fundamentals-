class Node: 
    def __init__(self , value):
        self.value = value
        self.next = None
        #This creates a Node class that contains a value and reference (link) to the next value, initially set to None. "None" is a special value in Python that explicitly denotes the intentional lack of any value. 
head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")
#This instantiates an object of the Node class as the value for the variable head It then instantiates second and third objects of the node class, as the value for the instance attribute head.next and head.next.next .   
#This creates a link from the first, to the second, to the third.
print(head.value)
print(head.next.value)
print(head.next.next.value)
#The value of each Node value is printed.