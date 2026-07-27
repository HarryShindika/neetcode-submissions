class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use our knowledge of the 2 sum problem to solve this
        #  2 sum involves find the difference in btn target and current number
        #  in this case, we will look for the difference btn our target and sum of first 2 numbers

        # for constant loopkup time, turn list into dictionary with value : index pairing.

        # iterate over nums for i and j (in double for loop) (avoid using same values for i and j)

        # val = target - (nums[i] + nums[j]). if val in nums and nums[val] != i and nums[val] != j:
            # sol = [nums[i],nums[j],nums[k]]
            # res.append(sol)
        # return res

        numsdict = {val: idx for idx, val in enumerate(nums)}

        res = []

        # while j < len(nums):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                val = 0 - (nums[i]+nums[j])
                if val in numsdict and numsdict[val] != i and numsdict[val] != j:
                    grp = sorted([nums[i],nums[j],val])
                    if grp not in res:
                        res.append(grp)


        return res
