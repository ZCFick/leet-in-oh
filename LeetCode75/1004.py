#My initial solution
def longestOnes(nums: list[int], k: int):
  i,j,count,zeros = 0,0,0,0
  max_count = 0
  while j<len(nums):
    if nums[j] == 1:
      count += 1
      j += 1
    else:
      if zeros<k:
        count += 1
        j += 1
        zeros += 1
      else:
        if i == j:
          j += 1
        else:
          if nums[i] == 0:
            zeros -= 1
        i += 1
        count = j-i
    max_count = max(max_count,count)
  return max_count

#Optimal solution
def longestOnes2(A: list[int], K: int) -> int:
  left = right = 0
  for right in range(len(A)):
    if A[right] == 0:
      K -= 1
    if K < 0:
      if A[left] == 0:
        K += 1
      left += 1
  return right - left + 1