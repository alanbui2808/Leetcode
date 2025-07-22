def solution(colors, k):
  '''
  Observation: Sliding window on circular array.
    (1). To deal with circular array, we can append the same array to the end.
    (2). However, the maximum elements we actually need are (K-1) elements.
      - We notice the starting of our window L is in range [0, N-1]. Thus the last L can be N-1, and
      it will span k-1 elements.
      - Example: [1 2 3 4] k = 2
                 [1 2 3 4][1] we need k-1 elements

        Because if we have [1 2 3 4][1 2 3 4]
                                     L => basically repeats.

  Algorithm:
    (1). Let L = 0
    (2). Let R: [1, N+k-2] aka [1, N+k-1)
    (3). Expand [L, R] if colors[R] != colors[R-1]
      - Note: R can be out of bound, aka colors[R] can be out of bound. However we can use R%N

    (4). If len of [L, R] == k: update result and shrink
    (5). In case colors[R] == colors[R-1]: we break the pattern. Update L = R and start new window.

  Time: O(N+k)
  Space: O(1)
  '''
  N = len(colors)
  M = N + (k-1)
  L = 0
  result = 0

  for R in range(1, M):
    # alterning
    if colors[R%N] != colors[(R-1)%N]:
      # enough elements
      if R-L+1 == k:
        result += 1
        L += 1

    # not alternating
    L = R

  return result






colors = [0,1,0,1,0]
k = 3
print(solution(colors, k))

