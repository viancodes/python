# Approach:
# 1. This is essentially a finite state check:
#    - A valid number may have: optional sign, digits, optional dot, optional exponent with sign & digits.
# 2. Track flags while scanning string:
#    - num_seen: at least one digit seen
#    - dot_seen: dot already appeared
#    - e_seen: exponent already appeared
#    - num_after_e: at least one digit after exponent
# 3. Iterate through characters and update flags according to rules.
# 4. Return True if num_seen is True and (if e_seen, also num_after_e is True).
# Time: O(n), Space: O(1)

class Solution:
    def isNumber(self, s):
        s = s.strip()
        num_seen = False
        dot_seen = False
        e_seen = False
        num_after_e = True
        
        for i, char in enumerate(s):
            if char.isdigit():
                num_seen = True
                if e_seen:
                    num_after_e = True
            elif char in ['+', '-']:
                # sign allowed only at start or right after 'e'/'E'
                if i != 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif char == '.':
                # dot not allowed if dot_seen or e_seen already
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif char in ['e', 'E']:
                # exponent not allowed if already seen or no number before
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_after_e = False  # must have digits after e
            else:
                return False
        
        return num_seen and num_after_e
