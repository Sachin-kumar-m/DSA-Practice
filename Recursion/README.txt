Recursion is heavily used in 
1. Merge sort,quick sort
2. BST, Binary Trees, Balanced BST, Tried etc
3. Graphs
4. Backtracking algorithms
5. Dynamic Programming problems

Calling a function again and agin until the base condition is satisfied is called Recursion

to implement recursion, we need to have a base condition in place. 

Solving a problem with small instance of the same problem

this is also called as bottom to top approach


Time complexity in recursive function is defined differently
if the function keeps breaking to (n-1),(n-2),(n-3)... then the time complexity is O(N)
if n/2,n/4 etc, then O(log(N))


Space complexity, we are storing all the function calls in a stack, so the size of the stack is my space,