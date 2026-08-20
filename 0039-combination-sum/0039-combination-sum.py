class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            # We found a valid combination
            if total == target:
                result.append(current[:])
                return

            # Sum is too large
            if total > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                # Choose the number
                current.append(num)

                # i instead of i + 1
                # because we can reuse the same number
                backtrack(i, current, total + num)

                # Undo the choice
                current.pop()

        backtrack(0, [], 0)

        return result