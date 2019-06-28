#!/usr/bin/env python
#Bao Dang
#Assignment 1

class arraystack:
    def __init__(self):
        self.maxlength = 10000
        self.elements = [None]*self.maxlength
        self.head = self.maxlength

    #clear the stack
    def makenull(self):
        self.head = self.maxlength

    #Check if the stack is empty
    def empty(self):
        if self.head >= self.maxlength:
            return True
        else:
            return False
    #Return the last element
    def top(self):
        if self.empty():
            print "Stack is empty"
        else:
            return self.elements[self.head]

    #Remove last element
    def pop(self):
        if self.empty():
            print "Stack is empty"
        else:
            self.head = self.head + 1

    #Add an element
    def push(self,x):
        if self.head == 0:
            print "Stack is full"
        else:
            self.head = self.head - 1
            self.elements[self.head] = x


if __name__ == "__main__":

    print "Create a new stack"
    test = arraystack()
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