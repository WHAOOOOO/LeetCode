class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
	# 删除排序数组中的重复项
        n = len(set(nums))
        i = 1
        while i < n:
            if nums[i] == nums[i - 1]:
                temp = nums[i]
                nums[i:len(nums)-1] = nums[i+1:]
                nums[-1] = temp
            else:
                i = i + 1
        return n
