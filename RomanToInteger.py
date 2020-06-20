# NOT original solution (need to revisit):

# I struggled with this problem, don't fully understand.
# Code copied from soln: "VERY simple python solution"

class Solution(object):
    def romanToInt(self, s):
        one_chars = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        two_chars = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        
        ans = 0
        ind = 0
        while ind < len(s):
            if ind+1 < len(s) and s[ind: ind+2] in two_chars:
                ans += two_chars[s[ind: ind+2]]
                ind += 2
            else:
                ans += one_chars[s[ind: ind+1]]
                ind += 1
        
        return ans
        