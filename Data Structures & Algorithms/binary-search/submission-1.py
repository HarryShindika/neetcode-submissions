class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # start in middle, check if middle is val
        # if true, return index of middle
        # if not, check if middle > target. if true, right == middle - 1
        # else, left = middle + 1

        l,r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1

