from executors import *
from services import Server, pingto
from tests import Ping
import yaml 

from constants import *

tup = (2,'Hi')
print(tup)
# Creamos un diccionario para añadir servidores
servers = {}
# Creamos un diccionario para añadir las pruebas de ping
pruebas_ping = {}

# Añadimos un servidor a manopla y una prueba de ping a manopla
google_server = Server('Google',('google.es',))
servers[google_server.name] = google_server
ping_google = Ping(TIMEOUT, TRIES, google_server)
pruebas_ping[google_server.name] = ping_google

# Abrimos el fichero prueba.yaml para añadir servidores y pruebas
# de ping a partir de lo que leeremos en este
with open ('prueba.yaml','r') as fichero_yaml:
    # Content es un diccionario
    content = yaml.load(fichero_yaml, Loader=yaml.FullLoader)
    for servers_dict in content['servers']:
        new_server = Server(servers_dict['name'], servers_dict['ips'])
        servers[new_server.name] = new_server
        prueba_ping = Ping(TIMEOUT, TRIES, new_server)
        pruebas_ping[new_server.name] = prueba_ping

# Nos creamos un Pool de ejecutores
pool_executors = PoolExecutors(5, list(pruebas_ping.values()),'test')
pool_executors.work()
pool_executors.work_finished()
print('Pruebas Finalizadas')

# Mostrar las pruebas realizadas
for prueba in pruebas_ping.values():
    print(prueba.res_list)