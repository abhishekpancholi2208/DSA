class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []
        
        i = 0
        while i<len(nums):
            j = i+1
            while j<len(nums):
                sum = nums[i]+nums[j]
                beg = j+1
                end = len(nums)-1
                while beg<end:
                    cursum = nums[beg]+nums[end]
                    if cursum == target - sum:
                        out.append([nums[i], nums[j], nums[beg], nums[end]])
                        beg += 1
                        while beg<end and nums[beg]==nums[beg-1]:
                            beg+=1
                        end -= 1
                    elif cursum > target - sum:
                        end -= 1
                    else:
                        beg += 1
                j+=1
                while j<len(nums) and nums[j] == nums[j-1]:
                    j+=1
            i+=1
            while i<len(nums) and nums[i] == nums[i-1]:
                i+=1
        return out
