#!/usr/bin/env python
#Bao Dang
#Assignment 1

from arraylist import *
from pointerlist import *
from arraystack import *
from pointerstack import *
import time

n = 3000

#Iterated insertion in front
def library_head():
    l = [0]*n
    start = time.time()
    for i in range(n):
        l.insert(0,1)
    stop = time.time()
    timetaken = (stop - start)*1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

def array_head():
    l = arraylist()
    start = time.time()
    for i in range(n):
        l.insert(1, 0)
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

def pointer_head():
    l = pointerlist()
    start = time.time()
    for i in range(n):
        l.insert(1, 0)
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

#Iterated insertation at the back

def library_tail():
    l = [0] * n
    start = time.time()
    for i in range(n):
        l.append(1)
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

def array_tail():
    l = arraylist()
    start = time.time()
    for i in range(n):
        l.insert(1, l.end())
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken


def pointer_tail():
    l = pointerlist()
    start = time.time()
    for i in range(n):
        l.insert(1, l.end())
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

# List traversal
def library_traversal():
    l = [0]*n
    start = time.time()
    for i in range(n):
        x = l[i]
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

def array_traversal():
    l = arraylist()
    for i in range(0, n):
        l.insert(1, l.end())
    p = l.first()
    start = time.time()
    while p:
        p = l.next_cell(p)
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

"""
def pointer_traversal():
    l = pointerlist()
    for i in range(0, n):
        l.insert(1, l.end())
    p = l.first()
    start = time.time()
    while p:
        p = l.next_cell(p)
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken"""

# Iterated deletion in front
def library_del_head():
    l = [0] * n
    start = time.time()
    for i in range(n):
        del l[0]
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken


def array_del_head():
    l = arraylist()
    for i in range(n):
        l.insert(1, l.end())
    start = time.time()
    for i in range(n):
        l.delete(0)
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

def pointer_del_head():
    l = pointerlist()
    for i in range(n):
        l.insert(1, l.end())
    start = time.time()
    for i in range(n):
        l.delete(0)
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken


#Iterated deletion at the back
def library_del_tail():
    l = [0] * n
    start = time.time()
    for i in range(n):
        l.pop()
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

def array_del_tail():
    l = arraylist()
    for i in range(n):
        l.insert(1, l.end())
    start = time.time()
    for i in range(n):
        l.delete(l.end())
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

def pointer_del_tail():
    l = pointerlist()
    for i in range(n):
        l.insert(1, l.end())
    start = time.time()
    for i in range(n):
        l.delete(l.end())
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

# Iterated stack insertions
def library_stack_push():
    s = []
    start = time.time()
    for i in range(n):
        s.append(1)
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

def array_stack_push():
    s = arraystack()
    start = time.time()
    for i in range(n):
        s.push(1)
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

def pointer_stack_push():
    s = pointerstack()
    start = time.time()
    for i in range(n):
        s.push(1)
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

# Iterated stack deletions
def library_stack_pop():
    s = []
    for i in range(n):
        s.append(1)
    start = time.time()
    for i in range(n):
        s.pop()
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

def array_stack_pop():
    s = arraystack()
    for i in range(n):
        s.push(1)
    start = time.time()
    for i in range(n):
        s.pop()
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

def pointer_stack_pop():
    s = pointerstack()
    for i in range(n):
        s.push(1)
    start = time.time()
    for i in range(n):
        s.pop()
    stop = time.time()
    timetaken = (stop - start) * 1000
    timetaken = "{:.4f}".format(timetaken)
    return timetaken

if __name__ == "__main__":
    print "Iterated Insertion of Library List in front performing time measurement ", library_head(), "ms"
    print "Iterated Insertion of Array List in front performing time measurement ", array_head(), "ms"
    print "Iterated Insertion of Pointer List in front performing time measurement ", pointer_head(), "ms"
    print "Iterated Insertion of Library List at the back performing time measurement ", library_tail(), "ms"
    print "Iterated Insertion of Array List at the back performing time measurement ", array_tail(), "ms"
    print "Iterated Insertion of Pointer List at the back performing time measurement ", pointer_tail(), "ms"
    print "Traversal of Library List performing time measurement ", library_traversal(), "ms"
    print "Traversal of Array List performing time measurement ", array_traversal(), "ms"
#    print "Traversal of Pointer List performing time measurement ", pointer_traversal(), "ms"
    print "Iterated Deletion of Library List in front performing time measurement ", library_del_head(), "ms"
    print "Iterated Deletion of Array List in front performing time measurement ", array_del_head(), "ms"
    print "Iterated Deletion of Pointer List in front performing time measurement ", pointer_del_head(), "ms"
    print "Iterated Deletion of Library List at the back performing time measurement ", library_del_tail(), "ms"
    print "Iterated Deletion of Array List at the back performing time measurement ", array_del_tail(), "ms"
    print "Iterated Deletion of Pointer List at the back performing time measurement ", pointer_del_tail(), "ms"
    print "Push operation of Library Stack performing time measurement ", library_stack_push(), "ms"
    print "Push operation of Array Stack performing time measurement ", array_stack_push(), "ms"
    print "Push operation of Pointer Stack performing time measurement ", pointer_stack_push(), "ms"
    print "Pop operation of Library Stack performing time measurement ", library_stack_pop(), "ms"
    print "Pop operation of Array Stack performing time measurement ", array_stack_pop(), "ms"
    print "Pop operation of Pointer Stack performing time measurement ", pointer_stack_pop(), "ms"