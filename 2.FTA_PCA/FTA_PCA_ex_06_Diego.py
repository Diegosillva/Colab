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
  print('#'*30)

  green = int(input('Digite 1 ou 0 para o sinalizador verde: '))
  red = int(input('Digite 1 ou 0 para o sinalizador vermelho: '))
  orange = int(input('Digite 1 ou 0 para o sinalizador laranja: '))
  conveyor = int(input('Digite 1 ou 0 para o esteira: '))
  
  verde = servidor.write_single_coil(4,green)
  vermelho = servidor.write_single_coil(5,red)
  laranja = servidor.write_single_coil(6,orange)
  esteira = servidor.write_single_coil(7,conveyor)
  sleep(1)