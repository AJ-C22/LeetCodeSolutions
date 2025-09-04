class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix[0])
        c = len(matrix)

        i = 0
        j = r * c - 1
        while i <= j:
            if not matrix or not matrix[0]:
                return False
            m = i + (j - i) // 2
            m_row = m // r
            m_col = m % r
            
            if matrix[m_row][m_col] < target:
                i = m + 1
            elif matrix[m_row][m_col] > target:
                j = m - 1
            else:
                return True
        return False


        