The following is a general backtracker parameterized by a solution array and a function for computing whether a given (partial) solution is acceptable. The backtracking engine is capable of solving the "no-equal-adjacent-substrings" and "N-queens" problems.

no-equal-adjacent-substrings: Generate a string of nn characters from the set {0,1,2} such that no two adjacent substrings are equal.
N-Queens: For each column in a chessboard, try to place N queens so that no two queens attack each other.
