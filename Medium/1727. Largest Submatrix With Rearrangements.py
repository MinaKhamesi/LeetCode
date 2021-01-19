def largestSubmatrix(self, matrix) -> int:
        if not matrix: return 0
        maxArea = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]:
                    matrix[row][col] = matrix[row - 1][col] + 1 if row > 0 else matrix[row][col]
            
            current = sorted(matrix[row] , reverse = True)
            for col in range(len(matrix[0])):
                maxArea = max(maxArea , current[col] * (col + 1))
        return maxArea