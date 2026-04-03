#My code, not fully time optimal but accurately uses stack
def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    i = 0
    while i<len(asteroids):
      if len(stack) == 0:
        stack.append(asteroids[i])
        i += 1
      if (asteroids[i]<0 and stack[-1]>0):
        if abs(asteroids[i])<abs(stack[-1]):
          i += 1
        elif abs(asteroids[i])>abs(stack[-1]):
          stack.pop()
        else:
          stack.pop()
          i+=1
      else:
        stack.append(asteroids[i])
        i+=1
    return stack