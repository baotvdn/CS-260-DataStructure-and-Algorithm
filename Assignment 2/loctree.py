#!/usr/bin/env python
#Bao Dang
#Assignment 2

class node:
    def __init__(self):
        self.label = None

class tree:
    def __init__(self):
        self.cellspace = [None]*maxnodes
        self.header = []
        self.root = 0

#PARENT: Find the parent of a node. Return None if the node is the root
def PARENT(n, T):
    if n == T.root:
        return None
    else:
        for i in range(len(T.header)):
            if n in T.header[i]:
                return i
            else:
                return None

#LEFTMOST_CHILD: Find the first child of a node. Return None if the node has no children
def LEFTMOST_CHILD(n, T):
    if T.header[n] is None:
        return None
    else:
        return T.header[n][0]

#RIGHT SIBLING: Find the right sibling of a node. Return None if the node is root or the right most child
def RIGHT_SIBLING(n, T):
    if n == T.root:
        return None
    else:
        i = PARENT(n, T)
        if (n in T.header[i]) and ((n+1) in T.header[i]):
            return n+1
        else:
            return None

#LABEL: Print the label
def LABEL(n, T):
    return T.cellspace[n].label

def ROOT(T):
    return T.root

def MAKENULL(T):
    T = tree()
    return T

#CREATE0: Return a tree that has 1 node
def CREATE0(v):
    temp = tree()
    temp.cellspace[temp.root] = node()
    temp.cellspace[temp.root].label = v

    temp.header.insert(0,[])

    return temp

#CREATE1: Return a tree that has another tree as its child
def CREATE1(v, T):
    temp = tree()

    temp.cellspace[temp.root] = node()
    temp.cellspace[temp.root].label = v

    temp.cellspace[temp.root+1] = node()
    temp.cellspace[temp.root+1] = T.cellspace[T.root]

    temp.header.insert(0,[temp.root+1])
    temp.header.insert(1,T.header)
    return temp

#CREATE2: Return a tree that has two other trees as its children
def CREATE2(v, T1, T2):
    temp = tree()
    temp.cellspace[temp.root] = node()
    temp.cellspace[temp.root].label = v

    temp.cellspace[temp.root + 1] = node()
    temp.cellspace[temp.root + 1] = T1.cellspace[T1.root]

    temp.cellspace[temp.root + 2] = node()
    temp.cellspace[temp.root + 2] = T2.cellspace[T2.root]

    temp.header.insert(0, [temp.root+1, temp.root+2])
    temp.header.insert(1, T1.header)
    temp.header.insert(2, T2.header)

    return temp

#CREATE3: Return a tree that has three other trees as its children
def CREATE3(v, T1, T2, T3):
    temp = tree()
    temp.cellspace[temp.root] = node()
    temp.cellspace[temp.root].label = v

    temp.cellspace[temp.root + 1] = node()
    temp.cellspace[temp.root + 1] = T1.cellspace[T1.root]

    temp.cellspace[temp.root + 2] = node()
    temp.cellspace[temp.root + 2] = T2.cellspace[T2.root]

    temp.cellspace[temp.root + 3] = node()
    temp.cellspace[temp.root + 3] = T3.cellspace[T3.root]

    temp.header.insert(0, [temp.root + 1, temp.root + 2, temp.root + 3])
    temp.header.insert(1, T1.header)
    temp.header.insert(2, T2.header)
    temp.header.insert(3, T3.header)
    return temp


if __name__ == "__main__":
    print "Create tree A with v = 8 "
    maxnodes = 100
    a = CREATE0(8)
    print "Check label of the root: "
    print LABEL(0,a)
    print "Check children"
    print a.header[0]

    print " Create tree B with v = 2 and tree A"
    b = CREATE1(2, a)
    print "Check labels of node 0 and node 1:"
    print LABEL(0,b)
    print LABEL(1,b)
    print "Check list of children of node 0 and node 1: "
    print b.header[0]
    print b.header[1]
    print "Check parent of node 1: "
    print PARENT(1,b)

    print " Create tree D with v = 5 and tree A, tree C(v=5)"
    c = CREATE0(5)
    d = CREATE2(12, a, c)
    print "Check labels of each node:"
    print LABEL(0, d)
    print LABEL(1, d)
    print LABEL(2, d)
    print "Check headers of each node:"
    print d.header[0]
    print d.header[1]
    print d.header[2]
    print "Check parents of node 1 and 2:"
    print PARENT(1,d)
    print PARENT(2,d)
    print "Check left most child of the root"
    print LEFTMOST_CHILD(0,d)
    print "Check right sibling of node 1"
    print RIGHT_SIBLING(1,d)

    print " Create tree E with v = 5 and tree A, tree B, tree C"
    e = CREATE3(20, a, b, c)
    print "Check labels of each node:"
    print LABEL(0, e)
    print LABEL(1, e)
    print LABEL(2, e)
    print LABEL(3, e)
    print "Check headers of each node:"
    print e.header[0]
    print e.header[1]
    print e.header[2]
    print e.header[3]
    print "Check parents of node 2:"
    print PARENT(2, e)
    print "Check left most child of the root"
    print LEFTMOST_CHILD(0, e)
    print "Check right sibling of node 2"
    print RIGHT_SIBLING(2, e)
    print "Check right sibling of node 3"
    print RIGHT_SIBLING(3, e)