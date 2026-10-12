from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, current_sum, path):
            # Base case: we found a valid combination
            if current_sum == target:
                result.append(list(path))
                return
            
            # Base case: the sum exceeded the target, no need to proceed
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same depth to prevent duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Choose the current candidate
                path.append(candidates[i])
                
                # Explore further, incrementing 'start' to i + 1
                backtrack(i + 1, current_sum + candidates[i], path)
                
                # Backtrack: remove the last chosen candidate and try the next one
                path.pop()

        # Sorting is crucial to group duplicates together
        candidates.sort()
        result = []
        backtrack(0, 0, [])
        return result