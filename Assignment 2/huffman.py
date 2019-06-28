#!/usr/bin/env python
#Bao Dang
#Assignment 2

"""Fot this problem, since the list python starts at 0, the forest is supposed to start at 0 """
class huffman_algorithm:
    def __init__(self):
        self.FOREST = []
        self.ALPHABET = []
        self.TREE = []
        self.least = 0
        self.second = 1
        self.lasttree = 0
        self.lastnode = 0

    def tree(self, leftchild=0, rightchild=0, parent=0):
        self.TREE.append([leftchild, rightchild, parent])
        self.lastnode = len(self.TREE)

    def alphabet(self, symbol, probability, leaf):
        self.ALPHABET.append([symbol, probability, leaf])

    def forest(self, weight, root):
        self.FOREST.append([weight, root])
        self.lasttree = len(self.FOREST)

    #find the trees that have smallest and second smallest weight
    def lightones(self):
        if self.FOREST[0][0] <= self.FOREST[1][0]:
            self.least = 0
            self.second = 1
        else:
            self.least = 1
            self.second = 0
        for i in range(2, self.lasttree):
            if self.FOREST[i][0] < self.FOREST[self.least][0]:
                self.second = self.least
                self.least = i
            elif self.FOREST[i][0] < self.FOREST[self.second][0]:
                self.second = i

    #create a new node with left child and right child that have smallest and second smallest weight
    def create(self, lefttree, righttree):
        self.tree()
        self.lastnode-=1
        self.TREE[self.lastnode][0] = self.FOREST[lefttree][1]
        self.TREE[self.lastnode][1] = self.FOREST[righttree][1]
        self.TREE[self.lastnode][2] = 0
        self.TREE[self.FOREST[lefttree][1]][2] = self.lastnode
        self.TREE[self.FOREST[righttree][1]][2] = self.lastnode
        return self.lastnode

    def huffman(self):
        while self.lasttree > 1:
            self.lightones()
            self.FOREST[self.least][0] = self.FOREST[self.least][0] + self.FOREST[self.second][0]
            self.FOREST[self.least][1] = self.create(self.least, self.second)
            self.FOREST[self.second] = self.FOREST[self.lasttree-1]
            self.FOREST.pop()
            self.lasttree -= 1

if __name__ == "__main__":

    A = huffman_algorithm()
    A.tree()
    A.tree()
    A.tree()
    A.tree()
    A.tree()
    A.alphabet('a', 0.07, 0)
    A.alphabet('b', 0.09, 1)
    A.alphabet('c', 0.12, 2)
    A.alphabet('d', 0.22, 3)
    A.alphabet('e', 0.23, 4)
    A.alphabet('f', 0.27, 5)
    A.forest(0.07, 0)
    A.forest(0.09, 1)
    A.forest(0.12, 2)
    A.forest(0.22, 3)
    A.forest(0.23, 4)
    A.forest(0.27, 5)

    print "FOREST TABLE"
    for n in A.FOREST:
        print n,
    print "\nALPHABET TABLE"
    for n in A.ALPHABET:
        print n,
    print "\nTREE TABLE"
    for n in A.TREE:
        print n,

    A.huffman()
    print "\n-------------\n"
    print "Result after doing Huffman"

    print "FOREST TABLE"
    for n in A.FOREST:
        print n,
    print "\nALPHABET TABLE"
    for n in A.ALPHABET:
        print n,
    print "\nTREE TABLE"
    for n in A.TREE:
        print n,
