class Solution:
    # @return an integer
    def atoi(self, str):
        valids = "1234567890"
        fminus = False
        i = 0
        while i < len(str):
            if str[i] in valids:
                break
            elif str[i] == '-':
                fminus = True
                i += 1
                break
            elif str[i] == '+':
                i += 1
                break
            elif str[i] in " \t":
                i += 1
            else:
                return 0

        j = i
        while j < len(str):
            if not str[j] in valids:
                break
            j += 1
            
        str = str[i:j]
        if len(str) == 0:
            return 0
            
        n = int(str)
        
        if fminus:
            n = -n
        if n > 2147483647:
            return 2147483647
        if n < -2147483648:
            return -2147483648
        return n


        
              

def test(s):
    sol = Solution()
    print sol.atoi(s)
    
test("")
test("-1")
test("+-2")  
test("2147483648")  
test("-2147483649") 
test("  -23")
test("  a21b")
        