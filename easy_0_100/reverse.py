class Solution:
    def reverse(self, x: int) -> int:
	# 整数反转
        a = -x
        b = ''
        c = ''
        if x == 0 or x < (-(2**31)) or x > ((2**31) - 1):
            return 0
        elif x > 0:
            for i in str(x):
                b = i + b
            if int(b) < (-(2**31)) or int(b) > ((2**31) - 1):
                return 0
            else:
                return int(b)
        elif x < 0:
            for i in str(a):
                c = i + c
            if -int(c) < (-(2**31)) or -int(c) > ((2**31) - 1):
                return 0
            else:
                return -int(c)
