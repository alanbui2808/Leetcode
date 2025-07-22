def solution(card_points, k):
  '''
  Observation:
  (1). Think about the problem backward, let's say we pick k times randomly from left or
  right. What we end up is a subarray of size N-k.
  (2). Thus we just need to find a subarray of size N-k that has  minimal sum.

  Algorithm: Sliding window (fixed size) + prefix sum
  (1). We start expanding our window until (R-L+1) = N-k
  (2). Then we calculate the sum by using prefix sum.
  (3). We update our window size by R += 1 and L += 1 since we want to remain a
  N-k window size

  Time Complexity: O(N)

  '''
  L = R = result = 0
  N = len(card_points)

  # O(N)
  ps = [i for i in card_points]
  for i in range(1, N):
    ps[i] += ps[i-1]

  if N-k == 0:
    return ps[-1]

  # Looking for subarray of size N-k that that has mininal sum
  # O(N)
  while R < N:
    if (R-L+1) < (N-k):
      R += 1

    else:
      # O(1)
      cur_sum = ps[R] - (ps[L-1] if L-1 >= 0 else 0)
      result = max(ps[-1] - cur_sum, result)

      # Change our window size:
      R += 1
      L += 1

  return result

#----------------------------------------------
card_points = list(map(int, input().split()))
k = int(input())
print(solution(card_points, k))







