# NOT original solution (need to revisit):

# I struggled with this problem, don't fully understand.
# Code copied from soln: "Simple python solution; runtime beats 99.75%"

def sumDigits(n):
    total = 0
    while n > 0:
        dig = n % 10
        total = total + dig * dig
        n = n // 10
    return total

class Solution(object):
    def isHappy(self, n):
        h = {}
        i = 1
        while i > 0:
            if sumDigits(n) == 1:
                return True
            else:
                if n in h:
                    return False
                else:
                    h[n] = n
                    n = sumDigits(n)