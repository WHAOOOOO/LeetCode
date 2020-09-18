class Solution:
    def isValid(self, s: str) -> bool:
	# 有效的括号
        d = {'(': ')', '[': ']', '{': '}'}
        iList = []
        if len(s) == 0 or len(s) / 2 != len(s) // 2:
            return False
        else:
            for i in s:
                if i in d:
                    iList.append(i)
                else:
                    if iList == [] or d[iList.pop()] != i:
                        return False
        return iList == []
