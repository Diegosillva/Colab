from time import sleep
from pyModbusTCP.client import ModbusClient as cliente

TM12 = '192.168.1.254' #252 TM5-900
TM5 = '192.168.1.252'
server_port = 502
device_id = 1

print('Testando a conexão.')

cliente_1 = cliente(host=TM12, port=server_port, unit_id=device_id)
cliente_2= cliente(host=TM5, port=server_port, unit_id=device_id)

if cliente_1.open() and cliente_2.open():
  print(f'Coneção com o robo {TM12} {server_port} estabelecida com sucesso')
  print(f'Coneção com o robo {TM5} {server_port} estabelecida com sucesso')
else:
  print('Error')
  exit()

sleep(1)


while True:
  print('#'*30)
  # TM12
  verde = cliente_1.read_discrete_inputs(3,1)[0]
  vermelho = cliente_1.read_discrete_inputs(4,1)[0]
  

  if (verde == True and vermelho == True):
    green = cliente_2.write_single_coil(4,1)
    green = cliente_2.write_single_coil(5,1)
    green = cliente_2.write_single_coil(6,1)
    print(f'Sinalizador Verde: {green}')
  else:
    green = cliente_2.write_single_coil(4,0)
    green = cliente_2.write_single_coil(5,0)
    green = cliente_2.write_single_coil(6,0)
    print(f'Sinalizador Verde: {green}')

  sleep(1)





'''
while True:
    # Entrada 3
    green_button = client1.read_discrete_inputs(3,1)[0]
    red_button = client1.read_discrete_inputs(4,1)[0]
    sleep(1)
    if(green_button==True and red_button==True):
         green_signal = client2.write_single_coil(4,1)
         green_signal = client2.write_single_coil(5,1)
         green_signal = client2.write_single_coil(6,1)
         print(f'Sinalizador Verde: {green_signal}')
    else:
        green_signal = client2.write_single_coil(4,0)
        green_signal = client2.write_single_coil(5,0)
        green_signal = client2.write_single_coil(6,0)
        print(f'Sinalizador Verde: {green_signal}')
'''  