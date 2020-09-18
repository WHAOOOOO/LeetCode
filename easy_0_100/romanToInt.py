class Solution:
    def romanToInt(self, s: str) -> int:
        '''直接当前字母与下一个字母判断，只要小于下一个字母则为负'''
        rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(s) - 1):
            if rome[s[i]] < rome[s[i+1]]:
                sum = sum - rome[s[i]]
            else:
                sum = sum + rome[s[i]]
        sum = sum + rome[s[-1]]
        return sum
