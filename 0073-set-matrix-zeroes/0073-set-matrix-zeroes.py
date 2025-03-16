class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeroes = []
        row_l = len(matrix[0])
        col_l = len(matrix)
        for i in range(col_l):
            for j in range(row_l):
                if matrix[i][j] == 0:
                    zeroes.append([i,j])

        for i in range(len(zeroes)):
            print(zeroes[i][0])
            matrix[zeroes[i][0]] = [0] * row_l

        for i in range(len(zeroes)):
            for j in range(col_l):
                matrix[j][zeroes[i][1]] = 0
        return

        

        