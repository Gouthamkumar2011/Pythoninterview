class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
myLinkedlist = LinkedList(1)
myLinkedlist.append(2)
myLinkedlist.append(3)
myLinkedlist.append(4)
myLinkedlist.append(5)

print(f'the middle node is: ', myLinkedlist.find_middle_node().value)