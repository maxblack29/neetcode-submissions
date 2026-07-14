class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [] # store answers
        nums.sort() # sort array
        

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip duplicates
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1 # too big so iterate right back bc sorted list

                elif threesum < 0:
                    l += 1
                
                elif threesum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                
                    l += 1
                    r -= 1 # iterate through
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 # skip duplicates in list
        return result