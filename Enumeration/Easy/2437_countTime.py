class Solution:
    def countTime(self, time: str) -> int:
        h1, h2, _, m1, m2 = time  # split the string

        # Calculate number of valid hours
        hour_count = 0
        for h in range(24):
            hh = f"{h:02d}"
            if (h1 == "?" or h1 == hh[0]) and (h2 == "?" or h2 == hh[1]):
                hour_count += 1

        # Calculate number of valid minutes
        minute_count = 0
        for m in range(60):
            mm = f"{m:02d}"
            if (m1 == "?" or m1 == mm[0]) and (m2 == "?" or m2 == mm[1]):
                minute_count += 1

        return hour_count * minute_count
