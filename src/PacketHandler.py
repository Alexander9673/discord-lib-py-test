import json

class PacketHandler:
  def __init__(self, shard, op, packet_data):
    self.shard = shard
    self.op = op
    self.packet_data = packet_data
    
    if self.op == 10:
      self.op_10()
    elif self.op == 11:
      self.op_11()
    elif self.op == 0:
      self.op_0()

  def op_10(self):
    data = {
      "op": 1,
      "d": self.shard.seq
    }

    self.shard.ws.send(json.dumps(data))

    data = {
      "op": 2,
      "d": {
        "token": self.shard.client.opts["token"],
        "properties": {
          "$os": "win32",
          "$device": "test",
          "$browser": "test"
        }
      }
    }

    self.shard.ws.send(json.dumps(data))

  def op_11(self):
    print("received opcode " + str(self.op))

  def op_0(self):
    print("received event " + self.packet_data.get("t"))