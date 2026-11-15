class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window, variable size

        long = 0
        l = 0
        chars = {}


        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r],0) + 1


            while r - l + 1 - max(chars.values()) > k:
                chars[s[l]] -= 1
                l += 1
            long = max(long,(r - l + 1))


        return long

            



