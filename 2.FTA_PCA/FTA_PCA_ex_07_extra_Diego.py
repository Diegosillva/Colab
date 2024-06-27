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
   point = client.write_float(9000,[450.00, 209.00, 223.00, -179.85, 2.69, 115.43])

   p1 = client.read_input_registers_float(point,1)[1]
   print(p1)
   

   sleep(1)

  