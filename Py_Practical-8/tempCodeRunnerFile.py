#20CE133 - Prachi Shah

"""Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method."""
class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def push(head, data):
    new_node = node(data, head)
    head = new_node
    return head

def pop(head):
    if head is None:
        return None
    data = head.data
    head = head.next
    return data, head

# traversal methods...
def traverse(head): 
    while head is not None:
        print(head.data)
        head = head.next

head = node(1, None) # Create a node with data 1
head = push(head, 6) # Push 6 into the stack
head = push(head, 9) 
head = push(head, 12) 
data, head = pop(head) # Pop the stack
traverse(head) # Print the stack
