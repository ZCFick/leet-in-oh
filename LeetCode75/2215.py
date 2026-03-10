#My original solution
def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
  answer = [[],[]]
  storage = dict()
  for x in nums1:
    storage[x] = [storage.get(x, [0,0])[0] + 1, storage.get(x, [0,0])[1]]
  for y in nums2:
    storage[y] = [storage.get(y, [0,0])[0], storage.get(y, [0,0])[1] + 1]
  for z in storage:
    if storage[z][0] == 0 and storage[z][1] > 0:
      answer[1].append(z)
    elif storage[z][1] == 0 and storage[z][0] > 0:
      answer[0].append(z)
  return answer

#Second, more optimal solution with set differences
def findDifference2(nums1: list[int], nums2: list[int]) -> list[list[int]]:
  set1, set2 = set(nums1),set(nums2)
  answer = [list(set1-set2), list(set2-set1)]
  return answer