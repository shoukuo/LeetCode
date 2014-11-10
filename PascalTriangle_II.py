class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        now = [1]
        next = []
        
        ith = 0
        while ith < rowIndex:
            ith += 1
            for col in range(0, ith + 1):
                if col == 0 or col == ith:
                    next.append(1)
                else:
                    next.append(now[col-1] + now[col])
            now = next[:]
            next = []
        
        return now

sol = Solution()
print sol.getRow(0)
print sol.getRow(1)
print sol.getRow(2)
print sol.getRow(3)
print sol.getRow(5)