#My solution, some optimal solutions use 2 pointer and a sort
def maxOperations(nums: list[int], k: int) -> int:
    seen = {}
    count = 0
    for x in nums:
      complement = k - x
      if seen.get(complement, 0) > 0:
        count += 1
        seen[complement] -= 1
      else:
        seen[x] = seen.get(x, 0) + 1
    return count