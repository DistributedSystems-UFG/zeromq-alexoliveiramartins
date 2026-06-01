import multiprocessing
import zmq, time
import sys
from minuto_a_minuto import flamengo, champions_league

SERVER_IP = "172.31.51.9"
SERVER_PORT = 1234

def server():
  context = zmq.Context()         
  socket = context.socket(zmq.PUB)          # create a publisher socket
  socket.bind(f"tcp://*:{SERVER_PORT}")     # bind socket to the address
  print(f"Publisher rodando na porta {SERVER_PORT}")
  mensagem = 0
  while True:                    
    time.sleep(5)                           # wait every 5 seconds
    t = "CHAMPIONS " + champions_league[mensagem]
    socket.send(t.encode())                 # publish the current time
    mensagem += 1

def client():
  context = zmq.Context()
  socket = context.socket(zmq.SUB)          # create a subscriber socket
  socket.connect(f"tcp://{SERVER_IP}:{SERVER_PORT}")   # connect to the server
  print(f"Subscriber conectado ao publisher {SERVER_IP}:{SERVER_PORT}")
  socket.setsockopt(zmq.SUBSCRIBE, b"CHAMPIONS") # subscribe to TIME messages

  for i in range(5):      # Five iterations
    time = socket.recv()  # receive a message related to subscription 
    print(time.decode())  # print the result      
#-
if __name__ == "__main__": #-
  if len(sys.argv) > 1 and sys.argv[1] == "server":
    server()
    sys.exit()
  if len(sys.argv) > 1 and sys.argv[1] == "client":
    client()
    sys.exit()

  s = multiprocessing.Process(target=server) #-
  c = multiprocessing.Process(target=client) #-
#-
  s.start() #-
  time.sleep(2) #-
  c.start() #-
  c.join() #-
  s.terminate() #-
