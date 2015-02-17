class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        pascal = []
        for row in range(0, numRows):
            piece = []
            for col in range(0, row + 1):
                if col == 0 or col == row:
                    piece.append(1)
                else:
                    piece.append(pascal[row-1][col-1] + pascal[row-1][col])
            pascal.append(piece)
        return pascal
        
sol = Solution()
print sol.generate(0)
print sol.generate(1)
print sol.generate(2)
print sol.generate(5)