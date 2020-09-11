class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        i = 0
        nums.reverse()
        while i < k:
            temp = nums.pop(0)
            nums.append(temp)
            i += 1
        nums.reverse()
