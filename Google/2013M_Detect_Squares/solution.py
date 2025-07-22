from collections import defaultdict

class DetectSquares:
  def __init__(self):
    '''
    Algorithm:
    (1). Store edges = {x: [y]} edges, where {x: y1, y2, y3} -> (x, y1), (x, y2), (x, y3)
    (2). Store count = {(x, y): #}

    Given (x1, y1):
    For y2 in edges[x1]:
    (1). We tried to 4 points (x1, y1), (x1, y2), (x2, y1), (x2, y2). We only need to calculate x2 = abs(y1-y2) +/- x1 (This is because
    it could be the left edge of square of right edge).
      (1.1). We notice that (x1, y1) and (x1, y2) forms an vertical edge, this is why we traverse through all y2 of given x1.
    (2). result = cnt[p2]*cnt[p3]*cnt[p4] (Note that when we call .count(), (x1, y1) not necessarily in the system).

    Time complexity provided below each function
    '''
    self.cnt = defaultdict(int) # {(x, y): #}
    self.edges = defaultdict(list) # {x: [y]} edges, where {x: y1, y2, y3} -> (x, y1), (x, y2), (x, y3)

  def add(self, point: list[int]) -> None:
    x, y = point
    cnt, edges = self.cnt, self.edges

    cnt[(x, y)] += 1
    # O(T) where T is number of add (edges)
    if y not in edges[x]:
      edges[x].append(y)

  def count(self, point: list[int]) -> int:
    '''
    p1: (x1, y1) - query point
    p2: (x1, y2)
    p3: (x2, y1)
    p4: (x2, y2)
    '''
    cnt, edges = self.cnt, self.edges

    x1, y1 = point
    result = 0

    # O(T) where T is number of add (edges)
    for y2 in edges[x1]:
      if y2 == y1:
        continue

      length = abs(y1 - y2)

      # Assume p1 and p2 forms the left edge of the square
      x2 = x1 + length
      p1, p2, p3, p4 = (x1, y1), (x1, y2), (x2, y1), (x2, y2)

      if p2 in cnt and p3 in cnt and p4 in cnt:
        result += cnt[p2] * cnt[p3] * cnt[p4]

      # Assume p1 and p2 forms the right edge of the square
      x2 = x1 - length
      p1, p2, p3, p4 = (x1, y1), (x1, y2), (x2, y1), (x2, y2)

      if p2 in cnt and p3 in cnt and p4 in cnt:
        result += cnt[p2] * cnt[p3] * cnt[p4]

    print(result)
    return result
#--------------------------------------------------------
solution = DetectSquares()
solution.add([3, 10])
solution.add([11, 2])
solution.add([3, 2])
solution.count([11, 10])
solution.add([14, 8])
solution.add([11, 2])
solution.count([11, 10])
