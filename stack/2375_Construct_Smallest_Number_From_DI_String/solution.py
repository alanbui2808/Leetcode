def solution(pattern):
  '''
  Observation: Greedy.
    1. If len(pattern) = N, then we need at most 1 -> N+1 digits, we need more.
    2. https://www.youtube.com/watch?v=GgN8d22BEf0 - Neetcode explanation

  '''
  N = len(pattern)
  res, stack = [], []

  for i in range(N+1):
    # at i, we deal upto i+1 elements.
    stack.append(i+1) # appand no matter what

    while stack and (i==N or pattern[i]=="I"): # stack will contains N+1 element
      res.append(str(stack.pop()))

  return "".join(res)
#-------------------------
pattern = "DDIDID"
print(solution(pattern), " expected: 3215476")
