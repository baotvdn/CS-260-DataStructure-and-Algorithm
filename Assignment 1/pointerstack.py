#!/usr/bin/env python
#Bao Dang
#Assignment 1

class cell:
    def __init__(self):
        self.element = None
        self.next = None

class pointerstack:
    def __init__(self):
        self.head = None

    # Return the last element
    def top(self):
        if self.empty():
            print "The stack is empty"
        else:
            return self.head.element

    # Remove last element
    def pop(self):
        if self.empty():
            print "The stack is empty"
        else:
            self.head = self.head.next

    # Add an element
    def push(self,x):
        if self.empty():
            new_element = cell()
            new_element.element = x
            self.head = new_element
        else:
            new_element = cell()
            new_element.element = self.head.element
            new_element.next = self.head.next
            self.head.element = x
            self.head.next = new_element

    # Check if the stack is empty
    def empty(self):
        if self.head is None:
            return True
        else:
            return False

    # clear the stack
    def makenull(self):
        self.head = None

if __name__ == "__main__":

    print "Create a new stack"
    test = pointerstack()
    print "Check if it is empty"
    print test.empty()
    print "Pushing 1-10"
    for i in range(1, 11):
        test.push(i)
    print "The top element is "
    print test.top()
    print "Pop 3 times"
    test.pop()
    test.pop()
    test.pop()
    print "Now the top element is"
    print test.top()
    print "Check if it is empty"
    print test.empty()
    print "Popping last 7 elements. Empty now?"
    test.pop()
    test.pop()
    test.pop()
    test.pop()
    test.pop()
    test.pop()
    test.pop()
    print test.empty()
    print "Try to pop one more element"
    test.pop()
    print "The top element now is"
    print test.top()
    print "Push some elements, then check makenull"
    test.push(1)
    test.push(2)
    test.push(3)
    test.makenull()
    print test.empty()
