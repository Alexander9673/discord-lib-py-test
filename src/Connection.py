import websocket
from . import PacketHandler as packet
import re
import threading as thread
import ssl
import json

def on_msg(shard):
  while shard.ws.connected:
    data = shard.ws.recv()

    if data != None or len(data) > 0:
      json_data = json.loads(data)
      packet.PacketHandler(shard, json_data.get("op"), json_data)

class Connection:
  def __init__(self, client, current_shard, index):
    self.id = current_shard
    self.index = index
    self.is_listening = False
    self.client = client
    self.seq = None
    self.ws = None

    self.connect()

  def connect(self):
    self.ws = websocket.create_connection("wss://gateway.discord.gg/?v=6", sslopt={"cert_reqs": ssl.CERT_NONE})
    
    try:
      th = thread.Thread(target=on_msg, args=[self], daemon=True)
      th.start()
      
      while th.is_alive():
        th.join(1)
    except KeyboardInterrupt:
      exit(1)