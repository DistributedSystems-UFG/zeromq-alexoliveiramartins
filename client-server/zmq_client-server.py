import multiprocessing #-
import zmq
from time import sleep #-
from cpf_validator import validateCPF

# cpfs para teste:
valido = "529.982.247-25"
invalido = "529.982.247-24"

def server():
  context = zmq.Context()
  socket  = context.socket(zmq.REP)       # create reply socket
  socket.bind("tcp://*:12345")            # bind socket to address

  while True:
    message = socket.recv()               # wait for incoming message
    if not "STOP" in str(message):        # if not to stop...
      msg = str(message.decode())
      valid = validateCPF(msg)
      if valid:
        reply = "CPF Valido"
      else:
        reply = "CPF Invalido"
      socket.send(reply.encode())         # send it away (encoded)
    else:                         
      break                               # break out of loop and end

def client():
  context = zmq.Context()
  socket  = context.socket(zmq.REQ)       # create request socket

  socket.connect("tcp://localhost:12345") # block until connected
  
  socket.send(valido.encode())             # send message
  message = socket.recv()                 # block until response
  print(message.decode)
  
  socket.send(invalido.encode())             # send message
  message = socket.recv()                 # block until response
  print(message.decode())

  socket.send(b"STOP")                    # tell server to stop
  print(message.decode())                 # print result
#-
if __name__ == "__main__": #-
  s = multiprocessing.Process(target=server) #-
  c = multiprocessing.Process(target=client) #-
#-
  s.start() #-
  sleep(2) #-
  c.start() #-
  c.join() #-
  s.join() #-
