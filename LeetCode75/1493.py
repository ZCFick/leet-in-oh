#Fairly fast solution
def longestSubarray(nums: list[int]) -> int:
  l, r, delete, zeros= 0, 0, 0, 0
  for r in range(len(nums)):
    if nums[r] == 0:
      delete += 1
      zeros += 1
    if delete > 1:
      if nums[l] == 0:
        delete -= 1
      l += 1
  if zeros == len(nums):
    return 0
  return r-l