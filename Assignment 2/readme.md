Programming Assignment 2 

Every student should choose a collection of problems with total number of points not exceeding 120. All points you gain above 100 count for extra credit and may compensate your lower performance on programming assignment 1.

(i) Implement the following basic data types. Follow specifications presented in the textbook in full detail.

(10 points) Queues: one implementation, pointer (pages 57-60), operations: FRONT, ENQUEUE, DEQUEUE, EMPTY, MAKENULL,
(20 points) Trees: two implementations, lists of children, leftmost-child right-sibling (pages 87-93), operations: PARENT, LEFTMOST_CHILD, RIGHT_SIBLING, LABEL, CREATEi (i=0,1,2,3), ROOT, MAKENULL.

(ii) Develop the code for the following timing experiments. Report your results in the form of a table. The first column should indicate the size of the input data. The remaining columns should report the measured times for the procedures that you apply. Derive conclusions out of your experiments and write them down.

(20 points) Perform time measurements of pre-order and post-order traversals of full trees of degree three and a given height. Run your code on both of your implementations of the tree ADT of problem number 2 of (i).

(iii) Implement algorithms solving the following problems just in terms of the List ADT operations. You need to use the code you developed for programming assignment 1.

(10 points) 2.3 b
(10 points) 2.4

(iv) You may implement algorithms solving the following problems either in terms of the ADT operations you developed for this class or any library data structures and algorithms available for C++ and Python. If you choose library tools you are allowed to use only those algorithms that from the point of view of accomplishing programming tasks do not exceed the ADT operations discussed in the textbook.

(20 points) 3.10 (hint: use a queue to store the children of visited nodes)

(15 points) 3.13 (assume that the label of each node consists of two fields: a unique integer identifying the node and an identifier l or i indicating whether a node is a leaf or an internal node)

(15 points) 3.14 ((a) prefix expression, (b) postfix expression)

(30 points) Huffman algorithm (3.4). For a given collection of characters and probabilities your program should create the Huffman tree and print out the codes for all the characters. Test your implementation on data provided in problem 3.20.

Each of the programs should contain test input data and a testing code, which demonstrate that all the operations and algorithms work properly. Use tree 3.31 (page 103) for testing the operations of the tree ADT and the solution of problem number 6. You will need to submit your solutions following the submission rules that will be provided at a later date.
