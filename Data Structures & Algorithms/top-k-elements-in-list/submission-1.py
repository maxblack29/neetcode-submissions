class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #empty tracker table for frequency
        result = []
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        pairs = list(count.items()) # creates iterable list of tuples for key value pairs
        pairs.sort(key = lambda x: x[1], reverse=True)
        for j in range(k):
            result.append(pairs[j][0])
        return result