class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
	# 两数之和
        new_List = []
        a = 0
        for i in nums:
            b = a + 1
            for j in nums[(a+1):]:
                if i + j == target:
                    if i + j == target:
                        new_List.append(a)
                        new_List.append(b)
                    else:
                        continue
                b += 1
            a += 1
        print(new_List)
        return new_List
