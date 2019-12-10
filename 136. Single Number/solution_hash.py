class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_dict = {}
        for i in nums:
            try:
                single_dict.pop(i)
            except:
                single_dict[i] = 1
        return single_dict.popitem()[0]