class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        buckets = []
        while len(buckets) <= len(nums):
            buckets.append([]) #add enough buckets in case worst case
            
        for num in count:
            freq = count[num]
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets)-1, 0, -1): #-1 is step
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        