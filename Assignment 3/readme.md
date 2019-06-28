Programming Assignment 3 

Each student group should choose a collection of problems with total number of points not exceeding 120. All points you gain above 100 count for extra credit and may compensate your lower performance on programming assignments 1,2.
Implement the following:

Dictionary ADT (4.5-4.8) with open hash tables (fig. 4.12) for problem 1 and closed hash tables (fig 4.14) for problem 2. Verify experimentally the following statements.

(20 points) For Dictionary ADT implemented with open hash tables the average number of probes required to make either a deletion or an insertion is O(1+ a). Find best numerical constants for deletion and insertion.

(20 points) For Dictionary ADT implemented with closed hash tables and the linear hashing as the rehash strategy the average number of probes required to make a deletion is approximately equal to (1+1/(1- a))/2 and the average number of probes required to make an insertion is approximately equal to (1+1/(1- a)2)/2.

In statements of problems 1 and 2 a = N/B is the load factor, N is the number of elements in the set, and B is the size of the bucket/hash table. It is recommended that you use library hash functions in your experiments.

(20 points) Dictionary ADT with BST's (5.1-5.2, figs 5.2-5.5). Verify experimentally that the average number of nodes on the path from the root to another node, in a random BST obtained by an iteration of INSERT operation is O(log2 n), where n is the number of items inserted into an initially empty BST. Assume that all permutations of elements are equally probable. It is recommended that you use library generators of random permutations.

(20 points) Trie (5.3) with a list representation for trie nodes (pages 167-168). Store the strings of the document Alice in Wonderland in your trie by iterating the INSERT operation and print out the size of the resulting trie (provide the exact definition of size that you use in your count).

(10 points) Dijkstra's shortest paths algorithm (6.3) with the adjacency matrix as the representation of the graph. Test your implementation on the graph of problem 6 of review 2.

(30 points) Dijkstra's shortest paths algorithm (6.3) with a partially ordered tree as a priority queue and linked adjacency lists as the representation of the graph. Test your implementation on the graph of problem 6 of review 2.
An implementation in C is described in section 9.8 of our CS 270 textbook Foundations of Computer Science by Alfred Aho and Jeffrey Ullman.
book chapters: http://infolab.stanford.edu/~ullman/focs.html 
C code: http://infolab.stanford.edu/~ullman/fcsc-figures.html
 
(10 points) Floyd's algorithm (6.4) with the option of recovering the paths. Test your implementation on the graph of problem 6 of review 2.

(10 points) Depth-first search algorithm (6.5) together with depth-first numbering of nodes. Test your algorithm on the graph of fig. 6.38, page 226.

(30 points) Fast Fourier Transform in two versions ([W] 2.5): dyadic size ([W] p.53) and any size ([W] p.55). Verify correctness of your implementations by comparing the results of your program with the results obtained with FFT's of standard mathematical packages.
Symbol [W] refers to the book Algorithms and Complexity by Herbert Wilf.
