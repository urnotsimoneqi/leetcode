# sort
# double pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        if nums is None or length < 3:
            return ans
        nums = sorted(nums)
        for i in range(length):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]: # remove duplication
                continue
            L = i + 1
            R = length - 1
            while L < R:
                sum = nums[i] + nums[L] + nums[R]
                if sum == 0:
                    ans.append([nums[i],nums[L],nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1 # remove duplication
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1 # remove duplication
                    L += 1
                    R -= 1
                elif sum < 0:
                    L += 1
                elif sum > 0:
                    R -= 1
        return ans