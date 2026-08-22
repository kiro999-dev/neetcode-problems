class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            start = i
            while(stack and stack[-1][0] > heights[i]):
                h,start = stack.pop()
                maxArea = max(maxArea,(i-start) * h)
            stack.append([heights[i],start])
        for i in range(len(stack)):
            h,start = stack.pop()
            maxArea = max(maxArea,(len(heights)-start) * h)
        return maxArea
        