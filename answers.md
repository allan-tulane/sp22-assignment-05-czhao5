# CMPS 2200 Assignment 5
## Answers

**Name:**______Chenyu Zhao _____


Place all written answers from `assignment-05.md` here for easier grading.

- **1a.**
-  This greedy algorithm is based on selecting the largest Geometrica denomination possible. Since the cycle is dropping to the next lower denonmination once the denomination before it can no longer be used, the cycle will continue until the change desired is acquired (exact change). If the coin denonmination ends up being 1, then it should produce as few coins as possible. 
-  
- **1b.**
  - work is W(n) = O(log_2(N))
  - span is S(n) = O(log_2(N))

- **2a.**
  One simple counterexample is the demoniations = {1,4,6,8} and N = 10 where the greedy algorithms uses 8, 1, and 1 to get N = 10. The minimum number of coins the greedy algorithms would return would be 3 coins. The actual minimum number of coins is not 3, but 2 as N = 10 could have been made with 4 and 6. Therefore, the greedy algorithm cannot work optiomally. 

- **2b.**
 From the counterexample given in 2a, let n = N and c = number of coins:
    - span is S(n) = O(n * c)
    - work is W(n) = O(n * c)
- **3a.**
 The optimal substructure property for this version of the edit distance problem and modified MED is :
   1. When S[0] = T[0], then MED(S[1:], T[1:])
   2. When S[0] does not equal T[0], then
      1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:],T[1:]))
      #insert, delete, and substitute in the respective order



