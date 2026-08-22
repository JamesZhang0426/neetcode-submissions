class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix)-1
        row = - 1 
        while left <= right:
            mid = (left+right) // 2
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                row = mid
                break
        if row == -1:
            return False 
        
        rowleft = 0
        rowright = len(matrix[row])-1 
        while rowleft <= rowright:
            mid = (rowleft+rowright) // 2

            if matrix[row][mid] == target:
                return True 
            elif target > matrix[row][mid]:
                rowleft = mid +1 
            elif target < matrix[row][mid]:
                rowright = mid -1 
        
        return False

        
