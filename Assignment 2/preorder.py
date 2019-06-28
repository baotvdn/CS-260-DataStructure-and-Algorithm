#!/usr/bin/env python
#Bao Dang
#Assignment 2

import sys
def preorder_evaluation(L):
    stack = []
    for i in range(len(L)-1, -1, -2):
        if L[i].isdigit():
            stack.append(L[i])
        else:
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            if L[i] == '+':
                stack.append(op1+op2)
            elif L[i] == '-':
                stack.append(op1-op2)
            elif L[i] == '*':
                stack.append(op1*op2)
            elif L[i] == '/':
                stack.append(op1*1.0/op2)
            else:
                print "There are wrong Operators"
    return stack[0]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Number of argument is not 2"
        sys.exit(1)
    else:
        test = sys.argv[1]
        print preorder_evaluation(test)

