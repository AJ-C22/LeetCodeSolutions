class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        l = len(mat)
        c = len(mat[0])

        row_counts = [0] * l
        col_counts = [0] * c

        value_to_position = {}
        for i in range(l):
            for j in range(c):
                value_to_position[mat[i][j]] = (i, j)

        for i, val in enumerate(arr):
            if val in value_to_position:
                r, col = value_to_position[val]
                row_counts[r] += 1
                col_counts[col] += 1

                if row_counts[r] == c or col_counts[col] == l:
                    return i

        return len(arr)