class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        x = (len(nums))
        i = 0
        while i<x:
            if nums[i] == val:
                nums.pop(i)
                x-=1
                continue
            i += 1
        return len(nums)