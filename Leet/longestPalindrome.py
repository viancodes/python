def longestPalindrome(s: str) -> str:
    def expandFromCenter(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # slice the valid palindrome

    longest = ""
    for i in range(len(s)):
        # Odd length palindrome (center at i)
        odd_pal = expandFromCenter(i, i)
        # Even length palindrome (center between i and i+1)
        even_pal = expandFromCenter(i, i + 1)
        # Update longest if needed
        if len(odd_pal) > len(longest):
            longest = odd_pal
        if len(even_pal) > len(longest):
            longest = even_pal

    return longest
