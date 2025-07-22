def solution(nums):
  '''
  Observation: Prefix sum
  '''
  N = len(nums)
  result = 0
  ps = [num for num in nums]

  for i in range(1, N):
    ps[i] += ps[i-1]

  for i in range(N-1):
    result += (ps[i] >= ps[N-1]-ps[i])

  return result

nums = list(map(int, input().split()))
print(solution(nums))
