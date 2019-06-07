import threading

class Proxy2Client(threading.Thread):
   mProxyUtil = None

   def __init__(self, proxyUtil):
      super().__init__()
      self.mProxyUtil = proxyUtil
      
   
   def run(self):
      while True:
         data = self.mProxyUtil.mClientSocket.recv(4096)
         toServer = True
         self.mProxyUtil.capturedTraffic(data, toServer)
         self.mProxyUtil.mServerSocket.send(data)
