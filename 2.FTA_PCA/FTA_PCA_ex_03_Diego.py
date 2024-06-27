from time import sleep
from pyModbusTCP.client import ModbusClient as cliente


server_ip = '192.168.1.252' #252 TM5-900
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
  print('='*20)

  start_tools = servidor.read_holding_registers(9000,1)[0]
  print(f'Start Ferramenta: {start_tools}')
 
  grip = servidor.read_holding_registers(9001,1)[0]
  print(f'Start Grip: {grip}')

  release = servidor.read_holding_registers(9002,1)[0]
  print(f'Release: {release}')

  qtd_pecas = servidor.read_holding_registers(9003,1)[0]
  for qtd in qtd_pecas:
   print(f'Quantidade de peças: {qtd}')


  cond_esteira = servidor.read_holding_registers(9004,1)[0]
  print(f'Condição da Esteira: {cond_esteira}')

  sleep(1)



