# 3Sum
# https://leetcode.com/problems/3sum/


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:  # 0 < nums[i] < nums[j] < nums[k]
                break
            if i > 0 and nums[i] == nums[i - 1]:  # we skip duplicates
                continue

            j: int = i + 1
            k: int = len(nums) - 1

            while j < k:
                s: int = nums[i] + nums[j] + nums[k]

                if s == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j = j + 1
                    while j < k and nums[k] == nums[k + 1]:
                        k = k - 1
                elif s < 0:
                    j = j + 1
                    while j < k and nums[j] == nums[j - 1]:
                        j = j + 1
                else:
                    k = k - 1
                    while j < k and nums[k] == nums[k + 1]:
                        k = k - 1

        return result
