class Solution:
    def maxArea(self, heights: List[int]) -> int:

        def getvol(l,r):
            return min(heights[l],heights[r]) * (r-l)

        l = 0 
        r = len(heights) - 1

        max_vol = 0
            
        while l < r:

            max_vol = max(getvol(l,r),max_vol)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_vol







