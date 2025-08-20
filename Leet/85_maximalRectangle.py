# Approach:
# 1. Treat each row as the base of a histogram:
#    - Build heights[j] = consecutive '1's up to current row for each column j.
# 2. For each row's heights, compute Largest Rectangle in Histogram via monotonic stack.
#    - Maintain increasing stack of indices; when current height < top, pop and compute area.
# 3. Track max area across all rows.
# Time: O(rows * cols), Space: O(cols).

class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for r in range(rows):
            # Update histogram heights for this row
            for c in range(cols):
                if matrix[r][c] == '1' or matrix[r][c] == 1:
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Compute largest rectangle in current histogram
            max_area = max(max_area, self._largestRectangleArea(heights))

        return max_area

    def _largestRectangleArea(self, heights):
        stack = []  # indices with increasing heights
        max_area = 0
        # Append sentinel 0 to flush the stack
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
