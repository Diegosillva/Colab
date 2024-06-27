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

stop = servidor.write_single_coil(7105,True)