class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):  
        s = s.lower()
        s_new = ""
        validChar = "abcdefghijgklmnopqrstuvwxyz0123456789"
        
        for c in s:
            if c in validChar:
                s_new += c

        if len(s_new) <= 1:
            return True
            
        l = 0
        r = len(s_new) - 1
        while r > l:
            if s_new[l] == s_new[r]:
                l = l + 1
                r = r - 1
            else:
                return False
        return True
        
sol = Solution()
s1 = "A man, a plan, a canal: Panama"
print sol.isPalindrome(s1)
s2 = "race a car"
print sol.isPalindrome(s2)
s3 = ""
print sol.isPalindrome(s3)
s4 = "a"
print sol.isPalindrome(s4)
s5 = "aba"
print sol.isPalindrome(s5)
s6 = ".G?j!:;;:Gj?!."
print sol.isPalindrome(s6)
