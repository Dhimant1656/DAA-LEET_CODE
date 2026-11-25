class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            if height[left] < height[right]:
                current_height = height[left]
                left += 1
            else:
                current_height = height[right]
                right -= 1

            area = width * current_height
            if area > max_area:
                max_area = area

        return max_area