from collections import defaultdict

def solution(heights):
  '''
  Observation: Simple monotonic stack

  '''
  N = len(heights)
  stk = [] # strictly decreasing monotonic stack
  res = [0 for i in range(N)]

  for i in range(N):
    while stk and heights[stk[-1]] < heights[i]:
      res[stk[-1]] += 1
      stk.pop()

    if stk:
      res[stk[-1]] += 1

    stk.append(i)

  return res



heights = [10,6,8,5,11,9]
print(solution(heights), ' expected: [3,1,2,1,1,0]')

heights = [5,1,2,3,10]
print(solution(heights), ' expected: [4,1,1,1,0]')