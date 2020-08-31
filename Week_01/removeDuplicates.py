class Solution:
    def removeDuplicates(self, nums) -> int:
        i, j= 0, 1
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                j = j + 1
            else:
                i = i + 1
                nums[i] = nums[j]
        return i+1