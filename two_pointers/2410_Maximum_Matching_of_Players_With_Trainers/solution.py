def solution(players, trainers):
  '''
  Observation: Greedily match the players and trainers.
    - Sort p and t in ascending order.
    - Always match the p[i] with the smallest t[j] s.t t[j] >= p[i]

  '''
  N, M = len(players), len(trainers)
  players.sort()
  trainers.sort()

  i = j = 0

  while i<N and j<M:
    if trainers[j] >= players[i]:
      i += 1
      j += 1

    elif trainers[j] < players[i]:
      j += 1

  return i