class Logger:
  def __init__(self):
    '''
    Algorithm:
    Once a message comes:
    (1). Record its timestamp
    (2). If message never appears --> set a waitime for this message = timestamp + 10
    (3). Else check if the current message's timestamp has passed its waitime
    '''
    self.waitime = {}

  def shouldPrintMessage(self, timestamp: int, message: str):
    if message not in self.waitime:
      self.waitime[message] = timestamp + 10
      return True
    else:
      if timestamp >= sel.waitime[message]:
        self.waitime[message] = timestamp + 10
        return True
      else:
        return False
