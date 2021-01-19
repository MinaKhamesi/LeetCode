#####84
def largestRectangleArea(self, heights) -> int:
        maxArea = 0
        stack = []
        for i , height in enumerate(heights):
            if not len(stack) or stack[-1][1] < height:
                stack.append([i , height])
            else:
                while stack and stack[-1][1] >= height:
                    idx , h = stack.pop()
                    maxArea = max(maxArea , h * (i - idx))
                    startIdx = idx
                stack.append([startIdx , height])
        while stack:
            idx , h = stack.pop()
            maxArea = max(maxArea , h * (len(heights) - idx))
        return maxArea