class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(left, right):
            if left > right:
                return -1 # left pointer passes right pointer

            mid = (left + right) // 2 # find mid pointer

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid +1 
                return binarysearch(left, right) 
            else:
                right = mid-1
                return binarysearch(left, right)
        
        return binarysearch(0, len(nums)-1)