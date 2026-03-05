
#My Solution
def moveZeroes(nums: list[int]):
  """Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array."""
  n = len(nums)
  i = 0
  count = 0
  while i<n:
    if nums[i] == 0:
      nums.pop(i)
      n-=1
      count +=1
      continue
    i+=1
  temp = [0]*count
  nums += temp
  return

#Optimal Solution
def moveZeroes2(nums: list[int]):
  i = 0
  for j in range(len(nums)):
    if nums[j] != 0:
      nums[j], nums[i] = nums[i], nums[j]
      i += 1
  return