# Approach:
# 1. The matrix has special properties:
#    - Each row is sorted.
#    - First element of each row > last element of previous row.
#    => The matrix can be treated as a flattened sorted array of size m*n.
# 2. Apply Binary Search on range [0, m*n - 1].
#    - Map 1D index → 2D indices: row = mid // n, col = mid % n
#    - Compare matrix[row][col] with target.
# 3. Time: O(log(m*n)), Space: O(1).

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
