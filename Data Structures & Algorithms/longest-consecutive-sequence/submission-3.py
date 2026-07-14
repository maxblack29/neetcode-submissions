class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first guess is to sort this
        if not nums:
            return 0
        z = sorted(nums) # return new sorted list
        count = 1 # counter
        highest = 1 # store highest freq
        for i in range(len(nums)):
            if z[i] == z[i-1] + 1:
                count += 1
                highest = max(highest, count)
            elif z[i] == z[i-1]:
                continue # pass through
            else:
                count = 1
        return highest