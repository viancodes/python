class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        path = []

        def dfs(start, remain):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return

            prev = None
            for i in range(start, len(candidates)):
                # skip duplicates at the same depth
                if prev is not None and candidates[i] == prev:
                    continue
                val = candidates[i]
                if val > remain:
                    break
                path.append(val)
                dfs(i + 1, remain - val)  # i+1 because each number can be used once
                path.pop()
                prev = val

        dfs(0, target)
        return res
