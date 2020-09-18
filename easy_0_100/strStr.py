class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
	# 实现strStr()
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
