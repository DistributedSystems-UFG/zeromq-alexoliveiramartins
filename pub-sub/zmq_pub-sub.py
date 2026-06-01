import multiprocessing
import zmq, time
from minuto_a_minuto import flamengo, champions_league

def server():
  context = zmq.Context()         
  socket = context.socket(zmq.PUB)          # create a publisher socket
  socket.bind("tcp://*:12345")              # bind socket to the address
  mensagem = 0
  while True:                    
    time.sleep(5)                           # wait every 5 seconds
    t = "CHAMPIONS " + champions_league[mensagem]
    socket.send(t.encode())                 # publish the current time
    mensagem += 1

def client():
  context = zmq.Context()
  socket = context.socket(zmq.SUB)          # create a subscriber socket
  socket.connect("tcp://localhost:12345")   # connect to the server
  socket.setsockopt(zmq.SUBSCRIBE, b"CHAMPIONS") # subscribe to TIME messages

  for i in range(5):      # Five iterations
    time = socket.recv()  # receive a message related to subscription 
    print(time.decode())  # print the result      
#-
if __name__ == "__main__": #-
  s = multiprocessing.Process(target=server) #-
  c = multiprocessing.Process(target=client) #-
#-
  s.start() #-
  time.sleep(2) #-
  c.start() #-
  c.join() #-
  s.terminate() #-
