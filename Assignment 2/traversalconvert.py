#!/usr/bin/env python
#Bao Dang
#Assignment 2

#Convert preorder to postorder
def preorder_postorder(String):
    L = list(String)
    s = []
    Operators = ['+','-','*','/']
    for i in range(len(L)-1, -1, -2):
        if L[i] in Operators:
            op1 = s.pop()
            op2 = s.pop()
            temp =op1+" "+op2+" "+L[i]
            s.append(temp)
        else:
            s.append(L[i])
    return s[-1]

#Convert postorder to preorder
def postorder_preorder(String):
    L = list(String)
    s = []
    Operators = ['+','-','*','/']
    for i in range(0,len(L),2):
        if L[i] in Operators:
            op1 = s.pop()
            op2 = s.pop()
            temp = L[i]+" "+op2+ " "+op1
            s.append(temp)
        else:
            s.append(L[i])
    return s[-1]

#Convert preorder to inorder
def preorder_inorder(String):
    L = list(String)
    s = []
    Operators = ['+','-','*','/']
    for i in range(len(L)-1,-1,-2):
        if L[i] in Operators:
            op1 = s.pop()
            op2 = s.pop()
            temp = op1+" "+L[i]+" "+op2
            s.append(temp)
        else:
            s.append(L[i])
    return s[-1]


if __name__ == "__main__":
    print "Testing expression(in order): 6 / 2 - 4 - 3 * 1 + 2 * 2 * 1"
    print "Testing Preorder Listing into Postorder Listing"
    test = "* - / 6 2 - 4 3 * + 1 2 * 2 1"
    print preorder_postorder(test)
    print "Testing Postorder Listing into Preorder Listing"
    test = "6 2 / 4 3 - - 1 2 + 2 1 * * *"
    print postorder_preorder(test)
    print "Testing Preorder Listing into Inorder Listing"
    test = "* - / 6 2 - 4 3 * + 1 2 * 2 1"
    print preorder_inorder(test)

