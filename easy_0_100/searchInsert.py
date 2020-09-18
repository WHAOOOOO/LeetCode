class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
	# 搜索插入位置
        if target in nums:
            return nums.index(target)
        else:
            if nums[0] > target:
                return 0
            elif nums[-1] <= target:
                return len(nums)
            else:
                for i in range(len(nums)):
                    if (nums[i] <= target and target < nums[i + 1]) or nums[i + 1] is None:
                        return i + 1
