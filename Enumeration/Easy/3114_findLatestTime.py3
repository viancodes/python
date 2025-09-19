class Solution:
    def findLatestTime(self, s: str) -> str:
        h1, h2, _, m1, m2 = list(s)

        # Hours first digit
        if h1 == '?':
            if h2 == '?' or h2 <= '1':
                h1 = '1'
            else:
                h1 = '0'

        # Hours second digit
        if h2 == '?':
            if h1 == '1':
                h2 = '1'
            else:
                h2 = '9'

        # Minutes first digit
        if m1 == '?':
            m1 = '5'

        # Minutes second digit
        if m2 == '?':
            m2 = '9'

        return f"{h1}{h2}:{m1}{m2}"
