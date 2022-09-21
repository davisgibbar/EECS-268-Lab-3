#stack class(last in first out)
from Node import Node

#handles stack data structure
class stack_class:

#initializes top value
    def __init__(self):
        self._top = None

#adds values ontop of stack
    def push(self, entry):
        if self.is_empty():
            self._top = Node(entry)
        else:
            temp_node = self._top
            self._top = Node(entry)
            self._top.next = temp_node

#removes values from top of stack
    def pop(self):
        if self.is_empty():
            self._top = None
        else:
            temp = self._top.entry
            self._top = self._top.next
            return temp

#looks at value on top of stack
    def peek(self):
        if self._top != None:
            return self._top.entry
        else:
            raise RuntimeError('Stack Empty')

#determines if stack is empty
    def is_empty(self):
        if self._top == None:
            return True
        else:
            return False
