def solution(n, queries):
  '''
  Observation: Binary Decomposition and Prefix Product
    (1). Decompose n into list of smallest powers of 2.
    (2). Use prefix product to compute product in range [L, R]

  Time: O(logn + N)
    1. Binary Decomposition: logn
    2. Prefix product: N

  Space: O(logn + N)

  '''
  N = len(queries)
  MOD = 10**9+7
  pows = []
  res = []

  i = 1 # tracks power of 2
  while n>0:
    # LSB = 1
    if n%2==1:
      pows.append(i)

    # right-shift
    n //= 2
    i *= 2

  # prefix-product
  for i in range(1, len(pows)):
    pows[i] *= pows[i-1]

  for l, r in queries:
    prod = pows[r] // (pows[l-1] if l-1>=0 else 1)
    prod %= MOD
    res.append(prod)

  return res