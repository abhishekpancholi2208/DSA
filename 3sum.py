class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    if len(res) == 0 or res[-1] != [nums[i], nums[j], nums[k]]:
                        res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                elif s > 0:
