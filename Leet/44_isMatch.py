class Solution:
    def isMatch(self, s, p):
        i = j = 0          # pointers for s and p
        star = -1          # most recent '*' position in p
        match = 0          # position in s matched after last '*'

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                # direct match or single-char wildcard
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                # record star and the match position in s; try to match 0 chars first
                star = j
                match = i
                j += 1
            elif star != -1:
                # mismatch: backtrack to last '*', let '*' absorb one more char
                j = star + 1
                match += 1
                i = match
            else:
                return False

        # consume trailing '*' in pattern
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
