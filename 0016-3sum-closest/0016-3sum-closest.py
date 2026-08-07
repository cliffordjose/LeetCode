class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # If this sum is closer, update closest
                if abs(total - target) < abs(closest - target):
                    closest = total

                # Exact answer
                if total == target:
                    return total

                # Sum is too small
                elif total < target:
                    left += 1

                # Sum is too large
                else:
                    right -= 1

        return closest