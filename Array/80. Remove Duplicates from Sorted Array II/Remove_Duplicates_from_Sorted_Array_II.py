class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in nums:
            if i < 2 or j != nums[i - 2]:
                nums[i] = j
                i += 1
        return i


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        current = 1  # 新数组中有效位置的最后一位，新加入的数据应当写到current + 1
        for i in range(2, len(nums)):  # 从第三位开始循环，前两位无论如何都是要加入新数组的
            if nums[i] != nums[current - 1]:  # 符合条件，加入新数组
                current += 1
                nums[current] = nums[i]
        return current + 1
