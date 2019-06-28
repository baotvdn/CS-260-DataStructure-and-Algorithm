#!/usr/bin/env python
class arraylist:
    def __init__(self):
        self.maxlength = 10000
        self.elements = [None]*self.maxlength
        self.last = 0

    def first(self):
        return 0

    def end(self):
        return self.last

    def retrieve(self,p):
        if p > self.last or p < 0:
            print "Position does not exist"
        else:
            return self.elements[p]

    def locate(self,x):
        for q in range(self.last):
            if self.elements[q] == x:
                return q


    def next_cell(self,p):
        if p >= self.last or p < 0:
            return None
        else:
            return p + 1

    def previous(self,p):
        if p > self.last or p <= 0:
            return None
        else:
            return p - 1

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

    def delete(self,p):
        if 0 <= p <= self.last:
            for q in range(p,self.last):
                self.elements[q-1] = self.elements[q]
            self.last = self.last - 1

    def makenull(self):
        self.__init__()

