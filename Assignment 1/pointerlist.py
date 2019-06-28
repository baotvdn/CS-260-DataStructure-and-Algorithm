#!/usr/bin/env python
#Bao Dang
#Assignment 1

class cell:
    def __init__(self):
        self.elements = None
        self.next = None

class pointerlist:
    def __init__(self):
        self.head = None
        self.pos = None

    # Print the first position
    def first(self):
        return self.head

    # Print the last position
    def end(self):
        q = self.head
        if self.head is None:
            return None
        index = 0
        while q.next:
            q = q.next
            index += 1
        return index

    # Return the value of a position
    def retrieve(self,p):
        q = self.head
        index = 0
        for i in range(p):
            if q.next:
                q = q.next
                index += 1
        return q.elements

    # Locate a position of a value
    def locate(self,x):
        p = self.head
        index = 0
        while p:
            if p.elements == x:
                return index
            else:
                p = p.next
                index += 1
        return None

    # Return the next position
    def next_cell(self,p):
        q = self.head
        index = 0
        for i in range(p):
            if q.next:
                q = q.next
                index += 1
        return index + 1

    # Return the previous position
    def previous(self,p):
        q = self.head
        index = 0
        for i in range(p):
            if q.next:
                q = q.next
                index += 1
        return index - 1


    # Insert position
    def insert(self,x,p):
        if p is None:
            temp = cell()
            temp.elements = x
            temp.next = None
            self.head = temp
            self.pos = self.head
        elif p == 0:
            temp = cell()
            temp.elements = x
            temp.next = self.head
            self.head = temp
            self.pos = self.head
        else:
            temp = cell()
            temp.elements = x
            temp2 = self.head
            while temp2 and p > 1:
                temp2 = temp2.next
                p-=1
            temp.next = temp2.next
            temp2.next = temp

    # Delete a position
    def delete(self,p):
        temp = self.head
        if p == 0:
            self.head = temp.next
        elif p == self.end():
            if temp.next is None:
                self.makenull()
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
        else:
            while p > 1:
                temp = temp.next
                p -= 1
            temp.next = temp.next.next
        self.pos = self.head

    # Clear the list
    def makenull(self):
        self.head = None
        self.pos = None

if __name__ == "__main__":

    print "Insert 1-5"
    test = pointerlist()
    test.insert(1, 0)
    test.insert(2, 0)
    test.insert(3, 0)
    test.insert(4, 0)
    test.insert(5, 0)

    print "Delete the last numbers"
    test.delete(test.end())
    print "The last position is", test.end()

    print "Clear the list"
    test.makenull()
    test.insert("a", 0)
    test.insert("b", 1)
    test.insert("c", 2)
    test.insert("d", 3)
    test.insert("e", 4)
    print "Create a list: a, b, c, d, e"
    print "Print the last position", test.end()
    print "Retrieve the second element", test.retrieve(1)
    print "Locate the index of b: ", test.locate("b")
    print "Next position after 'd':", test.next_cell(3)
    print "Previous of 'd' index:", test.previous(test.locate("d"))