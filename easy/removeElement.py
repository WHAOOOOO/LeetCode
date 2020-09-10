class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
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
