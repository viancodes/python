class Solution:
    def longestPalindrome(self, s):
        def expandFromCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            odd_pal = expandFromCenter(i, i)
            even_pal = expandFromCenter(i, i + 1)

            if len(odd_pal) > len(longest):
                longest = odd_pal
            if len(even_pal) > len(longest):
                longest = even_pal

        return longest
