def maximalRectangle(self, matrix) -> int:
        if not matrix: return 0
        maxArea = 0
        for row in range(0 , len(matrix)):
            if row == 0:
                currentRow = [int(num) for num in matrix[0]] + [0]
            else:
                for col in range(len(matrix[0])):
                    currentRow[col] = currentRow[col] + 1 if matrix[row][col] == '1' else 0
            currentMax = 0
            stack = []
            for i, height in enumerate(currentRow):
                if not len(stack) or height > stack[-1][1]:
                    stack.append([i , height])
                else:
                    while stack and stack[-1][1] >= height:
                        idx , h = stack.pop()
                        currentArea = h * (i - idx)
                        currentMax = max(currentMax , currentArea)
                        startIdx = idx
                    stack.append([startIdx , height])
            maxArea = max(maxArea , currentMax)
        return maxArea