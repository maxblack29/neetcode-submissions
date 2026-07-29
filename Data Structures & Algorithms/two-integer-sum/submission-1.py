class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {} # create set w/ nums, doesn't pick up duplicates though?
        for i, num in enumerate(nums):
            res = target - num
            if res in check:
                return [check[res], i]
            check[num] = i