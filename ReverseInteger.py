class Solution:
    # @return an integer
    def reverse(self, x):
        fpos = True
        if x < 0:
            fpos = False
        v = abs(x)
        s = str(v)
        s = s[::-1]
        lv = long(s)
        if fpos == False:
            lv = -lv
        if lv > 2147483647 or lv < -2147483648:
            return 0
        return lv
        
def test(n):
    sol = Solution()
    print sol.reverse(n)

test(123)
test(-123)
test(1000000003111111111111111111111)
        