class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers, l and r
        # strip string of empty spaces
        # while l < r, compare values to each other. if no match, return False else move l and r

        # edge case: len(s) = 1. return True

        if len(s) == 1:
            return True

        s = "".join(s.split())
        print(s)

        l,r = 0, len(s) - 1

        while l < r:

            c1 = s[l].lower()
            c2 = s[r].lower()


            if not c1.isalnum():
                l += 1
                
            elif not c2.isalnum():
                r -= 1
                


            elif c1 != c2:
                return False
            else:
                r -= 1
                l += 1 
        
        return True



        