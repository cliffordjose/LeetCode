class Solution:
    def findTheString(self, lcp):
        n = len(lcp)

        # Basic validation
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa

        # Merge positions that must have the same character
        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    union(i, j)

        # Assign smallest possible characters
        char = [''] * n
        mp = {}
        nxt = ord('a')

        for i in range(n):
            p = find(i)
            if p not in mp:
                if nxt > ord('z'):
                    return ""
                mp[p] = chr(nxt)
                nxt += 1
            char[i] = mp[p]

        word = "".join(char)

        # Recompute LCP
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1

        # Validate
        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""

        return word