class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        length = len(matrix[0])
        start, end = 0, row*length - 1
        while start <= end:
            mid = (start + end) // 2
            r = mid // length
            c = mid % length
            val = matrix[r][c]
            if val == target: 
                return True
            elif val < target:
                start = mid + 1
            else: 
                end = mid - 1
        return False