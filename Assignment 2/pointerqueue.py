#!/usr/bin/env python
#Bao Dang
#Assignment 2

class cell:
    def __init__(self):
        self.element = None
        self.next = None

class queue:
    def __init__(self):
        self.front = cell()
        self.rear = cell()
        self.front = self.rear

    #Clear the queue
    def makenull(self):
        self.front = cell()
        self.front.next = None
        self.rear = self.front

    #Check if it is empty
    def empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    #Return the first element
    def front_element(self):
        if self.empty():
            print "queue is empty"
            return
        else:
            return self.front.next.element

    #Add an element to the queue
    def enqueue(self,x):
        self.rear.next = cell()
        self.rear = self.rear.next
        self.rear.element = x
        self.rear.next = None

    #Remove an element
    def dequeue(self):
        if self.empty():
            print "queue is empty"
        else:
            self.front = self.front.next

if __name__ == "__main__":
    print "Create a new queue"
    A = queue()
    print "Check if it is empty"
    print A.empty()
    print "Add 3 into the queue"
    A.enqueue(3)
    print "Check if the queue is still empty"
    print A.empty()
    print "Add 4 into the queue"
    A.enqueue(4)
    print "The front element is ", A.front_element()
    A.dequeue()
    print "Now remove 1 element. The front element now is", A.front_element()
    print "Make it empty"
    A.makenull()
    print "Is the queue is empty?"
    print A.empty()