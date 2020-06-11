from . import Connection as conn
import re

class Client:
  def __init__(self, token="", shard={}, auto_connect=True):
    if re.search(r"\w+\.\w+\.\w+", token) == None:
      # token not exists or invalid
      raise TypeError("invalid token")

    if not(hasattr(shard, "count")):
      shard["count"] = 1
    if not(hasattr(shard, "start_at")):
      shard["start_at"] = 0

    self.shard = shard
    #self.on_msg = on_msg

    #if not(callable(self.on_msg)):
      #raise TypeError("no on_msg callback given")

    self.opts = {}
    self.opts["token"] = token

    if auto_connect == True:
      self.connect()

  def connect(self):
    i = self.shard["start_at"]
    real_index = 0
    
    while i < self.shard["count"]:
      conn.Connection(self, i, real_index)
      i += 1
      real_index += 1