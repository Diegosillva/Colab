from time import sleep
from pyModbusTCP.client import ModbusClient as cliente

server_ip = '192.168.1.254' #252 TM5-900
server_port = 502
device_id = 1

print('Testando a conexão.')

servidor = cliente(host=server_ip, port=server_port, unit_id=device_id)

if servidor.open():
  print(f'Conexação com o robo {server_ip}: {server_port} estabelecida com sucesso')
else:
  print('Error')
  exit()

sleep(1)


while True:
  green_button = servidor.read_discrete_inputs(3,1)[0]
  print(f'Botão Verde: {green_button}')

  red_button = servidor.read_discrete_inputs(4,1)[0]
  print(f'Botão Vermelho: {red_button}')
  
  sensor1 = servidor.read_discrete_inputs(1,1)[0]
  print(f'Botão Verde: {sensor1}')
  sleep(1)