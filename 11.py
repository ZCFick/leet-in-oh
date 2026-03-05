def maxArea(height: list[int]) -> int:
  i,j = 0,len(height)-1
  m = (j-i)*(min(height[i],height[j]))
  while i<j:
    if height[i]<=height[j]:
      i += 1
    else:
      j-=1
    m = max(m, (j-i)*(min(height[i],height[j])))
  return m