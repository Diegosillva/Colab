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
  
  verde = servidor.read_coils(4,1)
  print(f'Sinalizador Verde: {verde}')

  vermelho = servidor.read_coils(5,1)
  print(f'Sinalizador Vermelho: {vermelho}')

  laranja = servidor.read_coils(6,1)
  print(f'Sinalizador Laranja: {laranja}')

  esteira = servidor.read_coils(7,1)
  print(f'Acionamento da esteira: {esteira}')
  sleep(1)