#!/usr/bin/env python
#Bao Dang
#Assignment 1

class arraylist:
    def __init__(self):
        self.maxlength = 10000
        self.elements = [None]*self.maxlength
        self.last = 0

    #Print the first position
    def first(self):
        return 0

    #Print the last position
    def end(self):
        return self.last

    #Return the value of a position
    def retrieve(self,p):
        if p > self.last or p < 0:
            print "Position does not exist"
        else:
            return self.elements[p]

    #Locate a position of a value
    def locate(self,x):
        for q in range(self.last):
            if self.elements[q] == x:
                return q

    #Return the next position
    def next_cell(self,p):
        if p >= self.last or p < 0:
            return None
        else:
            return p + 1

    # Return the previous position
    def previous(self,p):
        if p > self.last or p <= 0:
            return None
        else:
            return p - 1

    #Insert position
    def insert(self,x,p):
        if self.last >= self.maxlength:
            print "List is full"
        elif p > self.last or p < 0:
            print "Position does not exist"
        elif p == self.last:
            self.elements[p] = x
            self.last = self.last + 1
        else:
            self.elements[p+1:self.last+1] = self.elements[p:self.last]
            self.elements[p] = x
            self.last = self.last + 1

    #Delete a position
    def delete(self,p):
        if 0 <= p <= self.last:
            for q in range(p,self.last):
                self.elements[q-1] = self.elements[q]
            self.last = self.last - 1

    #Clear the list
    def makenull(self):
        self.__init__()


if __name__ == "__main__":
    print "Insert 1-5"
    test = arraylist()
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
    print "Locate the index of b:", test.locate("b")
    print "Next position after 'd':", test.next_cell(3)
    print "Previous of 'd' index:", test.previous(test.locate("d"))