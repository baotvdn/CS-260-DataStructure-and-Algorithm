#!/usr/bin/env python
#Bao Dang
#Assignment 2
import arraylist

def concatenate(lists):
    output = arraylist.arraylist()
    i = 0
    for i in range(lists.end()):
        sublist = lists.retrieve(i)
        for j in range(sublist.end()):
            element = sublist.retrieve(j)
            output.insert(element, output.last)
    return output

if __name__ == "__main__":
    test1 = arraylist.arraylist()
    test1.insert(0,0)
    test1.insert(12,1)
    test1.insert(63,2)
    test1.insert(81,3)
    test2 = arraylist.arraylist()
    test2.insert(132,0)
    test2.insert(51,1)
    test2.insert(31,2)
    test2.insert(92,3)
    tests = arraylist.arraylist()
    tests.insert(test1,0)
    tests.insert(test2,1)
    tests = concatenate(tests)
    for i in range(0, tests.end()):
        print tests.retrieve(i),