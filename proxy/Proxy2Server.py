import threading

class Proxy2Server(threading.Thread):
   mProxyUtil = None

   def __init__(self, proxyUtil):
      super().__init__()
      self.mProxyUtil = proxyUtil
      
   
   def run(self):
      while True:
         data = self.mProxyUtil.mServerSocket.recv(4096)
         toServer = False
         self.mProxyUtil.capturedTraffic(data, toServer)
         self.mProxyUtil.mClientSocket.send(data)
