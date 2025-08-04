def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        # If the character is already seen and its index is inside the window
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1  # Move the window start

        char_index[char] = right  # Update the last seen index of the character
        max_length = max(max_length, right - left + 1)

    return max_length
