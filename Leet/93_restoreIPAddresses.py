# Approach:
# 1) Backtracking: place 3 dots to form 4 segments.
# 2) Valid segment rules:
#    - length 1..3, numeric value 0..255
#    - no leading zeros unless the segment is exactly "0"
# 3) Prune by remaining length:
#    - rem_len must be between rem_parts and 3*rem_parts
# Time: O(3^4 * n) worst-case small; Space: O(1) extra (path up to 4).

class Solution:
    def restoreIpAddresses(self, s):
        res, path = [], []
        n = len(s)

        def valid(seg):
            # no leading zero unless "0"
            if len(seg) > 1 and seg[0] == '0':
                return False
            val = int(seg)
            return 0 <= val <= 255

        def backtrack(i):
            parts_left = 4 - len(path)
            rem = n - i
            # Prune: too few or too many chars left
            if rem < parts_left or rem > 3 * parts_left:
                return

            if len(path) == 4:
                if i == n:
                    res.append(".".join(path))
                return

            # Try segments of length 1..3
            for l in range(1, 4):
                if i + l > n:
                    break
                seg = s[i:i+l]
                if valid(seg):
                    path.append(seg)
                    backtrack(i + l)
                    path.pop()

        backtrack(0)
        return res
