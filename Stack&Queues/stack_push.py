#Stack_Push using Linked LISTs.
class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp =self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height +=1
    


my_stack = Stack(4)
my_stack.push(1)
my_stack.push(3)
my_stack.print_stack()

#Stack_Push using LISTs

# class Stack:
#     def __init__(self):
#         self.stack_list = []
        
#     def print_stack(self):
#         for i in range(len(self.stack_list)-1, -1, -1):
#             print(self.stack_list[i])

#     def push(self,value):
#         self.stack_list.append(value)
    
    



# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)

# my_stack.print_stack()