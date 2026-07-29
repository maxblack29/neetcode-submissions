class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        dup = set(nums)
        if len(dup) != len(nums):
            return True
        else:
            return False