class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # edge case: len(numbers) == 2: return [1,2]

        # 2 pointer question, l and r
        # while l < r:
        # add the 2 numbers , compare sum to target. if equal, return [l+1,r+1]
        # if sum > target, r -= 1, else l += 1

        l,r = 0, len(numbers) - 1

        while l < r:
            comp = numbers[l] + numbers[r]

            if comp == target:
                return [l+1,r+1]
            elif comp > target:
                r -= 1
            else:
                l += 1

        