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
   move_z = client.write_float(9000,[-100.00])
   move_j1 = client.write_float(9001,[30.00])

   z = client.read_input_registers_float(move_z,1)[0]
   j1 = client.read_input_registers_float(move_j1,1)[0]
   print(z)
   print(j1)
   

   sleep(1)

  