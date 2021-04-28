#Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such 
# that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, 
# such that the container contains the most water.
class Solution(object):
    def maxArea(self, height):
        area, i, j = 0, 0, len(height)-1
        while (i < j):
            if height[i] <= height[j]:
                res = height[i] * (j - i)
                i += 1
            else:
                res = height[j] * (j - i)
                j -= 1
            if res > area: 
                area = res
        return area