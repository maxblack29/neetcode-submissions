class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        toll = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            toll.append(cost[i] + min(toll[i-1], toll[i-2]))
        
        return min(toll[-1], toll[-2])