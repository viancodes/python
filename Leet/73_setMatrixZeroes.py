# Approach:
# 1. Naive: Use extra O(m+n) arrays to track rows & cols with zeros → update after scan.
# 2. Optimized (Constant Space):
#    - Use first row and first column as markers.
#    - Steps:
#       a) Check if first row and first column themselves need to be zeroed (store flags).
#       b) Traverse rest of matrix:
#          - If matrix[i][j] == 0 → set matrix[i][0] = 0 and matrix[0][j] = 0.
#       c) Traverse again (excluding first row/col):
#          - If matrix[i][0] == 0 or matrix[0][j] == 0 → set matrix[i][j] = 0.
#       d) Finally update first row and first column if needed (based on stored flags).
# 3. Time: O(m*n), Space: O(1).

class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Step b: mark zeros on first row/col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Step c: zero out cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step d: handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Step d: handle first col
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
