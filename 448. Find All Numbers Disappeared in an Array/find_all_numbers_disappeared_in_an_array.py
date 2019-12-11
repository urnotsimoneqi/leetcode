"""
将所有正数作为数组下标，置对应数组值为负值。那么，仍为正数的位置即为（未出现过）消失的数字。
举个例子：
原始数组：[4,3,2,7,8,2,3,1]
重置后为：[-4,-3,-2,-7,8,2,-3,-1]
结论：[8,2] 分别对应的index为[5,6]（消失的数字）
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
        