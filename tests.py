from datetime import datetime

from services import pingto

# Clase de Tests
class Test:
    def __init__(self, name, timeout):
        self.name = name
        self.timeout = timeout
        self.results_tests = []

    def test():
        pass

# Test de Ping
class Ping(Test):
    def __init__(self, timeout, tries, server):
        super().__init__('Ping ' + server.name, timeout)
        self.server = server
        self.tries = tries
        self.res_list = []

    # Funcion que va a realizar los Tests de Ping y los va a almacenar en un array
    # de objetos resultados
    def test(self):
        for ip in self.server.ips:
            for i in range(self.tries):
                (res,err) = pingto(self.timeout,ip)
                if res:
                    break
            resultado = ResultTest(res, self.server, ip)
            self.res_list.append(resultado)
        return resultado
    
    def __str__(self):
        return 'Test: ' + self.name

    def __repr__(self):
        return self.__str__()  

# Clase a devolver en los tests
class ResultTest():
    def __init__(self, result, server, ip):
        self.result = result
        self.timestamp = str(datetime.now())
        self.server = server
        self.ip = ip
    
    # Cuando le hacemos un str(objeto) este se convierta de esta manera
    def __str__(self):
        return '=== Test Result === ' + '\n' + \
                'TimeStamp: ' + self.timestamp + '\n' + \
                'Server: ' + self.server.name + '\n' + \
                'IP: ' + self.ip + '\n' + \
                'Result: ' + str(self.result) + '\n'

    # Cuando se muestre dentro de una tupla, lista o diccionario se muestre como en el str()
    def __repr__(self):
        return self.__str__()