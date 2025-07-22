def solution(g, s):
  '''
  Observation: Greedily distribute the cookies.
    - Sort g, s in ascending order.
    - Always give the cookie with min size s[j] >= g[i]

  '''
  N, M = len(g), len(s)
  g.sort()
  s.sort()
  i = j = 0

  while i<N and j<M:
    if s[j] >= g[i]:
      i += 1
      j += 1

    # this cookie cant be distributed.
    elif s[j] < g[i]:
      j += 1

  return i
#---------------------------
g = [1,2,3]
s = [1,1]
print(solution(g, s), ' expected: 1')

g = [1,2]
s = [1,2,3]
print(solution(g, s), ' expected: 2')

g = [10,9,8,7]
s = [5,6,7,8]
print(solution(g, s), ' expected: 2')
