def solution(target, position, speed):
  '''
  Observation:
    (1). Suppose we have 2 cars, c1 and c2:
        c2 ------  c1 ------  target

      We have:
      - t2: the time required for c2 to reach target. Calculated by (target-position)/speed
      - t1: the time required for c1 to reach target.

    (2). If t2 <= t1:
      - c2 will definitely catches up to c1.
      - c2 will merge into c1. c2 now travels same speed as c1.

    (3). t_merged = t1.
      - it requires c1 t1 time to reach the target, so t_merged must equal to t1

    => Merge currently element to the prev element. We use stack.

  Algorithm:
    1. Sort cars = [(position, speed)] in ascending order by position.
    2. Traverse backward in cars:
      - Calculate cur_t = target-pos/speed
      - Compare stk[-1]:
        - cur_t > stk[-1]: add cur_t into the stk
          => Basically means this car doesnt belong to the closest fleet.
        - otherwise: do nothing

    => We must traverse backward instead for this implementation.

  Time: O(NlogN + N)
  Space: O(N)


  '''
  N = len(position)
  stk = []

  cars = [(position[i], speed[i]) for i in range(N)]
  cars.sort() # sort by position, ascending

  for i in range(N-1, -1, -1):
    time = (target-cars[i][0])/cars[i][1]

    if not stk or (stk and time > stk[-1]):
      stk.append(time)

  return len(stk)
#------------------------------------
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(solution(target, position, speed), "expected: 3")

target = 10
position = [3]
speed = [3]
print(solution(target, position, speed), "expected: 1")

target = 100
position = [0,2,4]
speed = [4,2,1]
print(solution(target, position, speed), "expected: 1")

