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

# play_pause = client.write_single_coil(7104,1)

sleep(1)

while True:
    # Sensor 1
    x_coordenada = client.read_input_registers_float(7025,2)[0]
    y_coordenada = client.read_input_registers_float(7027,2)[0]
    z_coordenada = client.read_input_registers_float(7029,2)[0]
    print('*'*20)
    print(f'Coordenada: X {x_coordenada:.4f}')
    print(f'Coordenada: Y {y_coordenada:.4f}')
    print(f'Coordenada: Z {z_coordenada:.4f}')
    
    sleep(1)