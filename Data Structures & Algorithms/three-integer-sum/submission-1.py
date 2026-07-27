class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sorting takes O(N log N)
        res = []

        for i in range(len(nums) - 2):
            # Optimization: If the smallest number is > 0, three numbers can't sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers for the remaining sub-array
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res