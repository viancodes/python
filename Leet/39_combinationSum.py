class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        path = []

        def dfs(start, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                c = candidates[i]
                # Prune since candidates is sorted
                if total + c > target:
                    break
                path.append(c)
                # i (not i+1) because we can reuse the same number
                dfs(i, total + c)
                path.pop()

        dfs(0, 0)
        return res
