# Approach:
# 1. Sliding Window with counts:
#    - Need: frequency map of t.
#    - Expand right pointer; track how many chars meet required freq.
#    - When all required chars are satisfied, try to shrink from left to minimize.
# 2. Keep best (len, left, right) while shrinking.
# 3. Time: O(m+n), Space: O(k) where k = unique chars in t.

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""
        
        need = Counter(t)
        required = len(need)          # number of distinct chars to satisfy
        window = {}
        formed = 0                    # how many distinct chars currently satisfied
        
        l = 0
        best_len = float('inf')
        best = (0, 0)
        
        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            
            if ch in need and window[ch] == need[ch]:
                formed += 1
            
            # Try to shrink from the left while all requirements met
            while formed == required:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best = (l, r + 1)  # r+1 for slicing
                
                left_ch = s[l]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                l += 1
        
        return s[best[0]:best[1]] if best_len != float('inf') else ""
