class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        1. 列表是否为空
        2. 算出最短字符串长度
        3. 开始比较
        '''
        # if len(strs) == 0:
        #     return ""
        # elif len(strs) == 1:
        #     return strs[0]
        # else:
        #     minLen = len(strs[0])
        #     for i in strs:
        #         if len(i) < minLen:
        #             minLen = len(i)
        #     s = ""
        #     for i in range(minLen):
        #         a = strs[0][i]
        #         for j in range(len(strs)):
        #             if strs[j][i] != a:
        #                 return s
        #         s = s + a
        #     return s
        import os 
        return os.path.commonprefix(strs)
