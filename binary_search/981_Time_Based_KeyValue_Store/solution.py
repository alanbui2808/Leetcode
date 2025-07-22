from collections import defaultdict

class TimeMap:
  '''
  Observation: Binary search

  '''
  def __init__(self):
    # {key: list[tupple]}
    self.dict = defaultdict(list)

  def set(self, key: str, value: str, timestamp: int) -> None:
    self.dict[key].append((value, timestamp))

  def get(self, key: str, timestamp: int) -> str:
    lst = self.dict[key]
    L, R = 0, len(lst)-1
    res = ""

    while L <= R:
      mid = (L+R)//2

      # check timestamp at lst[mid]
      if lst[mid][1] <= timestamp: # a valid lst[mid]
        res = lst[mid][0]
        L = mid+1 # explore on the right since we're looking to maximize mid
      else:
        R = mid-1

    return res

#--------------------------------------------
obj = TimeMap()
commands = ["set","get","get", "set","get","get"]
values = [["foo","bar",1],["foo", 1], ["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
N = len(commands)
res = []

for i in range(N):
  c, v = commands[i], values[i]

  if c == "set":
    res.append(obj.set(v[0], v[1], v[2]))

  if c == "get":
    res.append(obj.get(v[0], v[1]))

print(res)
