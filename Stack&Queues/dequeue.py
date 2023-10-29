class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp =self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

myqueue = Queue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
print("first element dequeued: ",myqueue.dequeue())
print("second element dequeued: ",myqueue.dequeue())
print("third element dequeued: ",myqueue.dequeue())
print("fourth element dequeued: ",myqueue.dequeue())
