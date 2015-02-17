class Solution:
    # @return a string
    def convert(self, s, nRows):
        strd = {}
        for r in range(0, nRows):
            strd[r] = ""
            
        tlen = len(s)
        itr = 0
        while itr < tlen:
            for i in range(0, nRows):
                if itr >= tlen:
                    break
                strd[i] += s[itr]
                itr += 1
            for i in range(nRows-2, 0, -1):
                if itr >= tlen:
                    break
                strd[i] += s[itr]
                itr += 1
                
        str = ""
        for i in range(0, nRows):
            str += strd[i]
        
        return str

def test(s, n):
    sol = Solution()
    print sol.convert(s, n)

s = "PAYPALISHIRING"
test(s, 3)