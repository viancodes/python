# Approach (Monotonic Stack):
# 1. Maintain an increasing stack of indices by height.
# 2. When current height < height at stack top, pop and compute area with the popped bar as the smallest:
#    - height = heights[pop]
#    - width = i - (stack_top_after_pop) - 1
# 3. Append a sentinel 0 at the end to flush remaining bars.
# Time: O(n), Space: O(n).

class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # stores indices with increasing heights
        max_area = 0
        heights.append(0)  # sentinel to flush stack at the end

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left_index = stack[-1] if stack else -1
                width = i - left_index - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # remove sentinel
        return max_area
