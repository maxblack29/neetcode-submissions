class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remainder, cur_path, start):
            if remainder == 0:
                results.append(list(cur_path))
            if remainder < 0:
                return
            
            for i in range(start, len(nums)):
                cur_path.append(nums[i])
                backtrack(remainder-nums[i], cur_path, i)
                cur_path.pop()
            
        backtrack(target, [], 0)
        
        return results