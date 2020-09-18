class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
	# 移除元素
        '''
        1. 先计算去掉关键值之后的数组长度
        2. 使用while循环，如果是关键值则移到后边，计数器不变；如果不是关键值，计数器+1
        '''
        count = 0
        a = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count = count + 1
            else:
                continue
        nLen = len(nums) - count
        while a < nLen:
            if nums[a] == val:
                nums[a:len(nums) - 1] = nums[a+1:]
                nums[-1] = val
            else:
                a = a + 1
        return nLen
