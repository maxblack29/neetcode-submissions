class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        cur = 0
        max_area = 0
        for i in range(len(heights)):
            width = right - left
            height = min(heights[left], heights[right])
            cur = width * height # calculate max_area

            if cur > max_area:
                max_area = cur
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_area