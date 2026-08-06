class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        mini = float('inf')

        for i in nums:
            mini = min(mini,i)
        return mini
        