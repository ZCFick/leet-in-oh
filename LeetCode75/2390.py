#Both my solution and optimal solution
def removeStars(s: str) -> str:
  answer = []
  for x in s:
    if x == "*":
      answer.pop()
    else:
      answer.append(x)
  return "".join(answer)
