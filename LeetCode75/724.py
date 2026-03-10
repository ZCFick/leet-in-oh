#My original solution
def pivotIndex(nums: list[int]) -> int:
  sumLeft, sumRight = [0],[0]
  for x in range(1, len(nums)):
    sumLeft.append(sumLeft[x-1]+nums[x-1])
    sumRight.insert(0, sumRight[-x]+nums[-x])
  for x in range(0, len(nums)):
    if sumLeft[x] == sumRight[x]:
      return x
  return -1

#Optimal solution
def pivotIndex2(nums: list[int]) -> int:
  s,count=sum(nums),0
  for ind in range(len(nums)):
    count+=nums[ind]
    if count==s:
      return ind
    s-=nums[ind]
  return -1