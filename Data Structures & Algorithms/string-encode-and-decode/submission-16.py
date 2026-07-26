class Solution:

    def encode(self, strs: List[str]) -> str:

        # use a prefix containing the length of a string and a delimiter e.g. #
        # append this to every string, before joining the list ande returrn the encodede string

        res =[]
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)




    def decode(self, s: str) -> List[str]:
        # use the length of each string and the delimiter from above to separate the substrings
        # read through string until you hit the delimiter. The string s[i:j] will be the correct length of the
        # substring we need to decode
        # extract this substring, append to the output list, then repeat process, starting at character after delimiter
        # return output list

        res = []
        i = 0

        while i < len(s):
            j = i # starting the count for the length of the substring
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            start = j + 1
            end = start + length

            res.append(s[start:end])

            i = end

        return res
