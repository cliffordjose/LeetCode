class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def dfs(i, j):
            # We reached the end of the pattern
            if j == len(p):
                return i == len(s)

            # Check whether current characters match
            first_match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == '.')
            )

            # If the next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':

                # Option 1: '*' matches zero characters
                # Skip "x*"
                zero = dfs(i, j + 2)

                # Option 2: '*' matches one or more characters
                one_or_more = first_match and dfs(i + 1, j)

                return zero or one_or_more

            # Normal character or '.'
            if first_match:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)