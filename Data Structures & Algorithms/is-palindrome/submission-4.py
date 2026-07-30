class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers, l and r
        # strip string of empty spaces
        # while l < r, compare values to each other. if no match, return False else move l and r

        # edge case: len(s) = 1. return True

        if len(s) == 1:
            return True

        # s = "".join(s.split())
        # print(s)

        l,r = 0, len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1
                
            while l < r and not s[r].isalnum():
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False

            l += 1 
            r -= 1
        
        return True

        # TIME: O(n), you visit every character in string
        # SPACE: O(1), no new space is created



        