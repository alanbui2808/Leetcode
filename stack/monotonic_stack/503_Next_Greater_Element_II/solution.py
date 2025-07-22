def solution(nums):
  '''
  Observation: Monotonic stack similar to Next Greater Element
    - We can traverse at most N+N elements and handle just like before.

  '''
  N = len(nums)
  stk = []
  res = [-1 for i in range(N)]

  for i in range(N+N):
    # element i: N -> N+N will be mapped to i%N
    while stk and nums[stk[-1]] < nums[i%N]:
      res[stk.pop()] = nums[i%N]

    stk.append(i%N)

  return res
#-----------------------
nums = [1,2,1]
print(solution(nums), " expected: [2,-1,2]")
nums = [1,2,3,4,3]
print(solution(nums), " expected: [2,3,4,-1,4]")
nums = [1,3,2,4]
print(solution(nums), " expected: [3,4,4,-1]")
