import sys
from importlib import reload

import Disector

class ProxyUtil():
   mClientSocket = None
   mServerSocket = None

   def __init__(self, clientSocket, serverSocket):
      self.mClientSocket = clientSocket
      self.mServerSocket = serverSocket

   def capturedTraffic(self, data, toServer):
      dirrection = "->"
      if toServer == False:
         dirrection = "<-"
      print( "packet sent: " + str(dirrection))
      try:
         reload(Disector)
         Disector.Disector.parseBinary(data, toServer)
      except:
         print("Unexpected error:", sys.exc_info()[0])
