class Solution:
    def lengthOfLastWord(self, s):
        # Approach (notes):
        # 1) Skip trailing spaces from the end.
        # 2) Count chars until next space or start of string.
        # Time: O(n), Space: O(1)
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
