def solution(nums):
  '''
  Observation: We basically looking for multiple valid windows: [L, R]
    1. To grab all Ls, construct a decreasing stack.
      e.g: [5 3 4 2] => stk = [5 3 2]. 4 is ignored because whatever R matches with L, can match with 3 for better result.
      => Greedy.

    2. For each R: N-1 -> 0:
      e.g: Greedily pop L from stk until stk[-1] > R. For each L pop calculate R-L.
       The last L popped matches with this R to form the longest [L, R] in this range.

      - There might be valid windows [L', R'] but [L  [L'    R']  R] but these will always be less wild. You will notice this R' < R. So we will basically ignore these.

      - But later, we might find a R' able to pop L and even further to form better window: [L'   L   R'  R]. Notice this R' > R. Because only that R' can start poping L.
      => Also greedily

  Time: O(N)
  Space: O(N)


  '''
  N = len(nums)
  stk = []
  res = 0

  # Grab all the Ls
  for i in range(N):
    if stk and nums[stk[-1]] > nums[i]:
      stk.append(i)

  # process each R and find the longest window.
  for j in range(N-1, -1, -1):
    while stk and nums[stk[-1]] <= nums[j]:
      res = max(res, j - stk[-1])
      stk.pop()

  return res