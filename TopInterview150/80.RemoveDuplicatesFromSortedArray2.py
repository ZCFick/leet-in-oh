class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h = 0
        for x in nums:
            if h < 2 or x != nums[h-2]:
                nums[h] = x
                h += 1
        return h