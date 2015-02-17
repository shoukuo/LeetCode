class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        s = str(x)
        print s
        i = 0
        while i < len(s)/2:
            if s[i] != s[len(s)-1-i]:
                return False
            else:
                i += 1
        return True 
def test(n):
    sol = Solution()
    print sol.isPalindrome(n)

test(11)
test(121)
test(123)