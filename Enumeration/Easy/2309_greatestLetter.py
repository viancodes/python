class Solution:
    def greatestLetter(self, s: str) -> str:
        # Convert string to a set for O(1) membership checks
        letters = set(s)

        # Iterate from 'Z' to 'A' (reverse order)
        for ch in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if ch in letters and ch.lower() in letters:
                return ch
        
        return ""  # No match found
