from Float_Modbus import FloatModbusClient
from time import sleep

# Define device/robot parameters
SERVER_IP = '192.168.1.254' # TMrobot
SERVER_PORT = 502
DEVICE_ID = 1

# Establish TCP connection
print('Trying to establish connection.....')
client = FloatModbusClient(host=SERVER_IP, port=SERVER_PORT, auto_open=True)

if client.open():
    print("Connection to Robot %s:%d established succesfully" % (SERVER_IP, SERVER_PORT))
else:
    print("[Error] Fail to connect to modbus slave %s:%d." % (SERVER_IP, SERVER_PORT))
    exit()
# Define Parameters

play_pause = client.write_single_coil(7104,1)

sleep(1)

while True:
   
   time_01 = int(input('Digite o valor do WaitFor1 em (ms): '))
   time_02 = int(input('Digite o valor do WaitFor2 em (ms): '))
   time_03 = int(input('Digite o valor do WaitFor3 em (ms): '))
   sequencia = int(input('\nDigite o valor da seguencia: '))

   seg = client.write_single_register(9000, sequencia)
   verde = client.write_single_register(9001, time_01)
   vermelho = client.write_single_register(9002, time_02)
   laranja = client.write_single_register(9003, time_03)


   sleep(1)

  