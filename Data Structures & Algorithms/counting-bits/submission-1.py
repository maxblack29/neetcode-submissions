class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [] #initialize
        count = 0

        for i in range(0, n+1, 1):
            z = i
            while z > 0:
                z = z & (z-1) #flips last 1 to 0
                count += 1 # add count
            result.append(count)
            count = 0 #reset count

        return result