#!/usr/bin/env python
#Bao Dang
#Assignment 2

class node:
    def __init__(self):
        self.label = None
        self.leftmost_child = None
        self.right_sibling = None
        self.parent = None

class tree:
    def __init__(self):
        self.cellspace = [None]*maxnodes
        self.root = None

#PARENT: Find the parent of a node. Return None if the node is the root
def PARENT(n, T):
    try:
        return T.cellspace[n].parent
    except:
        return None

#LEFTMOST_CHILD: Find the first child of a node.
def LEFTMOST_CHILD(n, T):
    try:
        return T.cellspace[n].leftmost_child
    except TypeError:
        return None

#RIGHT SIBLING: Find the right sibling of a node.
def RIGHT_SIBLING(n , T):
    try:
        return T.cellspace[n].right_sibling
    except TypeError:
        return None

#LABEL: Print the label
def LABEL(n, T):
    return T.cellspace[n].label

#CREATE0: Return a tree that has 1 node
def CREATE0(v):
    temp = tree()

    temp.root = v
    temp.cellspace[temp.root] = node()
    temp.cellspace[temp.root].label = v

    return temp

#CREATE1: Return a tree that has another tree as its child
def CREATE1(v, T):
    temp = tree()

    temp.root = v
    temp.cellspace[temp.root] = node()
    temp.cellspace[temp.root].label = v
    temp.cellspace[temp.root].leftmost_child = T.root

    temp.cellspace[T.root] = node()
    temp.cellspace[T.root] = T.cellspace[T.root]
    temp.cellspace[T.root].parent = temp.root

    return temp

#CREATE2: Return a tree that has two other trees as its children
def CREATE2(v, T1, T2):
    temp = tree()
    temp.root = v

    temp.cellspace[temp.root] = node()
    temp.cellspace[temp.root].label = v
    temp.cellspace[temp.root].leftmost_child = T1.root

    temp.cellspace[T1.root] = node()
    temp.cellspace[T1.root] = T1.cellspace[T1.root]
    temp.cellspace[T1.root].right_sibling = T2.root
    temp.cellspace[T1.root].parent = temp.root

    temp.cellspace[T2.root] = node()
    temp.cellspace[T2.root] = T2.cellspace[T2.root]
    temp.cellspace[T2.root].parent = temp.root

    return temp

#CREATE3: Return a tree that has three other trees as its children
def CREATE3(v, T1, T2, T3):
    temp = tree()
    temp.root = v

    temp.cellspace[temp.root] = node()
    temp.cellspace[temp.root].label = v
    temp.cellspace[temp.root].leftmost_child = T1.root

    temp.cellspace[T1.root] = node()
    temp.cellspace[T1.root] = T1.cellspace[T1.root]
    temp.cellspace[T1.root].right_sibling = T2.root
    temp.cellspace[T1.root].parent = temp.root

    temp.cellspace[T2.root] = node()
    temp.cellspace[T2.root] = T2.cellspace[T2.root]
    temp.cellspace[T2.root].right_sibling = T3.root
    temp.cellspace[T2.root].parent = temp.root

    temp.cellspace[T3.root] = node()
    temp.cellspace[T3.root] = T3.cellspace[T3.root]
    temp.cellspace[T3.root].parent = temp.root

    return temp


def ROOT(T):
    return T.root

def MAKENULL(T):
    T = tree()
    return T


if __name__ == "__main__":
    print "Create tree A with v = 8 "
    maxnodes = 100
    a = CREATE0(8)
    print "Check label of the root: "
    print LABEL(8, a)

    print "Create tree B with v = 2 and tree A"
    b = CREATE1(2, a)

    print "Check parent of node node"
    print PARENT(8, b)
    print "Check most left child of B"
    print LEFTMOST_CHILD(2 ,b)

    print "Create tree d with v = 7 and tree A, tree B"
    d = CREATE2(7, a, b)
    print "Check parent of node 2"
    print PARENT(2, d)
    print "Check left most child of node 7"
    print LEFTMOST_CHILD(7, d)
    print "Check right sibling of node 8"
    print RIGHT_SIBLING(8, d)