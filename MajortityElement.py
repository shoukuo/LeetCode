class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        maj = None
        count = 0
        piv = len(num)/2
        for n in num:
            if count == 0:
                maj = n
                count += 1
            elif n == maj:
                count += 1
            else:
                count -= 1
                
            if count > piv:
                break
        return maj

def test(l):
    sol = Solution()
    print sol.majorityElement(l)
    
a = [1, 2, 3, 4, 1, 1, 1, 1,1]
test(a)