class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        maxSub = 0
        thisSum = 0
        for n in A:
            thisSum += n
            if thisSum < 0:
                thisSum = 0
            if thisSum > maxSub:
                maxSub = thisSum
        return maxSub
        
def test(A):
    sol = Solution()
    print sol.maxSubArray(A)
    
test([-2,1,-3,4,-1,2,1,-5,4])
