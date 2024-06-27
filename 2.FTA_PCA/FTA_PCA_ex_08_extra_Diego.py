from Float_Modbus import FloatModbusClient
from time import sleep

# Define device/robot parameters
SERVER_IP1 = '192.168.1.254'#{'TM12': '192.168.1.254', 'TM5':'192.168.1.252', 'Turck_1':'192.168.1.3', 'Turck_2': '192.168.1.4'}# TMrobot
SERVER_IP2 = '192.168.1.252'#{'TM12': '192.168.1.254', 'TM5':'192.168.1.252', 'Turck_1':'192.168.1.3', 'Turck_2': '192.168.1.4'}# TMrobot
SERVER_IP3 = '192.168.1.3'#{'TM12': '192.168.1.254', 'TM5':'192.168.1.252', 'Turck_1':'192.168.1.3', 'Turck_2': '192.168.1.4'}# TMrobot
SERVER_IP4 = '192.168.1.4'#{'TM12': '192.168.1.254', 'TM5':'192.168.1.252', 'Turck_1':'192.168.1.3', 'Turck_2': '192.168.1.4'}# TMrobot
SERVER_PORT = 502
DEVICE_ID = 1



# Establish TCP connection
print('Trying to establish connection.....')
client_TM12 = FloatModbusClient(host=SERVER_IP1, port=SERVER_PORT, auto_open=True)
client_TM5 = FloatModbusClient(host=SERVER_IP2, port=SERVER_PORT, auto_open=True)
client_Turck_01 = FloatModbusClient(host=SERVER_IP3, port=SERVER_PORT, auto_open=True)
client_Turck_02 = FloatModbusClient(host=SERVER_IP4, port=SERVER_PORT, auto_open=True)

if client_TM12.open() and client_TM5.open() and client_Turck_01.open() and client_Turck_02.open():
    print("Connection to Robot %s:%d established succesfully" )
else:
    print("[Error] Fail to connect to modbus slave %s:%d." )
    exit()
# Define Parameters

play_pause = client_TM5.write_single_coil(7104,1)

sleep(1)

while True:
   
  #turck02
  sensor_1 = client_Turck_02.read_discrete_inputs(2,1)[0]
  sensor_2 = client_Turck_02.read_discrete_inputs(8,1)[0]
  #TM12
  sensor_esteira_TM12 = client_TM12.read_discrete_inputs(7,1)[0]
  #TM5
  sensor_esteira_TM5 = client_TM5.read_discrete_inputs(7,1)[0]
  ponto_b_tm5 = client_TM5.read_holding_registers(9001, 1)[0]
  ponto_b_tm12 = client_TM5.read_holding_registers(9001, 1)[0]


  if sensor_1 == 1 and sensor_2 == 1 and sensor_esteira_TM5 == 1 and sensor_esteira_TM12 == 1:
    levar_produto_TM12 = client_TM12.write_single_register(9000, 1)
    levar_produto_TM5 = client_TM5.write_single_register(9000, 1)
  else:
     
     levar_produto_TM12 = client_TM12.write_single_register(9000, 0)
     levar_produto_TM5 = client_TM5.write_single_register(9000, 0)

  if ponto_b_tm5 == 1 and  ponto_b_tm12 == 1:
     client_Turck_01.write_single_coil(4,1)

     


     
     
  #turck01
  # sinalizador = client_Turck_01.read_discrete_inputs(4,1)[0]
  # botao = client_Turck_01.read_discrete_inputs(6,1)[0]

  sleep(1)
  