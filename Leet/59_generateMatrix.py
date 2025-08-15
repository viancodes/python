class Solution:
    def generateMatrix(self, n):
        # Approach (notes):
        # Fill layers in spiral order with a running number from 1..n^2.
        # Maintain four bounds: top, bottom, left, right. Shrink after each side.
        # Time: O(n^2), Space: O(1) extra (besides output matrix)
        mat = [[0]*n for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        num = 1
        while top <= bottom and left <= right:
            # left -> right
            for c in range(left, right+1):
                mat[top][c] = num; num += 1
            top += 1
            # top -> bottom
            for r in range(top, bottom+1):
                mat[r][right] = num; num += 1
            right -= 1
            if top > bottom or left > right:
                break
            # right -> left
            for c in range(right, left-1, -1):
                mat[bottom][c] = num; num += 1
            bottom -= 1
            # bottom -> top
            for r in range(bottom, top-1, -1):
                mat[r][left] = num; num += 1
            left += 1
        return mat
