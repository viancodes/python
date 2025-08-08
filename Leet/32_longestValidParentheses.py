class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]  # Initialize with base index
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # Reset base index
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
