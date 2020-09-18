class Solution:
    def isPalindrome(self, x: int) -> bool:
	# 回文数
        if x < 0:
            return False
        elif x >= 0 and x < 10:
            return True
        else:
            a = 0
            for i in range(len(str(x))):
                if int(str(x)[i]) == int(str(x)[len(str(x)) - 1 - i]):
                    continue
                else:
                    a = 1
            if a == 0:
                return True
            else:
                return False
