import socket

from Proxy2Client import Proxy2Client
from Proxy2Server import Proxy2Server
from ProxyUtil import ProxyUtil

#class Proxy():
#   __init__(self, dstServerIp, dstServerPort, dstClientIp, dstClientPort)



dstClientIp = "127.0.0.2"
dstClientPort = 3333
dstServerIp = "master.pwn3"
dstServerPort = 3333

serverSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
clientSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

#wait until client establishes a connection
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
clientSocket.bind((dstClientIp, dstClientPort))
socketQueue = 5
clientSocket.listen(socketQueue)
clientGameSocket, clientIp = clientSocket.accept()

#connect to the real server
randomClientPort = 15347
serverSocket.bind((socket.gethostname(), randomClientPort))
serverSocket.connect((dstServerIp, dstServerPort))
serverGameSocket = serverSocket

utils = ProxyUtil(clientGameSocket, serverGameSocket)
clientThread = Proxy2Client(utils)
serverThread = Proxy2Server(utils)

clientThread.start()
serverThread.start()

clientThread.join()
serverThread.join()

