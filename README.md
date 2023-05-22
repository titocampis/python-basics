# Python Basics

## 0. Contents

## 1. Introduction

### 1.1 Interpreted Programming Language

Python es un lenguaje de programación interpretado, es decir, su código fuente se ejecuta direc- tamente, instrucción a instrucción. El código no pasa por un proceso de compilación, sino que tenemos un programa llamado intérprete que lee la instrucción en tiempo real, y la ejecuta. Los archivos de Python se llaman módulos y se identifican mediante la extensión de archivo .py. Un módulo puede definir funciones, clases y variables.

### 1.2 How does python works?

Python es un interprete de codigo, es decir, hace de intermediario entre el programador y el Sistema Operativo convirtiendo el código python en algo interpretable para el SO que hay por debajo (linux)

Cuando nosotros ejecutamos en nuestro terminal un python3 .... Lo que estamos haciendo es pedirle a nuestro SO que arranque un hilo del binario python3 para que interprete ficheros .py y los ejecute (transforme en ordenes entendibles y concretas para el SO).

### 1.3 Download and Execute Python

1. Download python3:

```bash
$ sudo apt update && sudo apt upgrade
$ sudo sudo apt upgrade python3
```

2. Install pip

```bash
$ sudo apt install python3-pip
```

3. Execute a python module (named xxx.py)

```bash
$ python3 xxx.py
```

### 1.4 Python Comments

```python
'''
This is a big comment in python
'''
# This is a small comment in python
# :P
```

## 2. Data Structure

### 2.1 Variable Naming Convention

* Las variables van todas en minuscula (a no ser que sean constantes)
* Las variables que contengan varias palabras estas iran separadas siempre por "_"
* Las constantes iran siempre con todas sus letras en mayusculas

:page_facing_up: **EXAMPLE:**

```python
CONSTANTE_1 = 123
variable = 'Hola'
diccionario_de_compras = {'pantalones' : 24,
                          'camiseta' : 19}
```

>:mega: **NOTA:**
>
>Python no necesita definir previamente el tipo de dato que será, es suficiente con declararlo en el momento de la creación, algunos ejemplos:
>```python
>a = 10000
>b = 1e9
>c = 0.000008
>d = 'hola'
>e = (1,4,7,9,17)
>f = [19,8,7,4,9]
>```

### 2.2 Booleans

* True
* False
* true y fase no son nada

### 2.3 Tuples

Secuencias ordenadas e **inalterables** de datos (no se pueden añadir ni modificar datos)

* Es posible la mezcla de tipos de datos

:page_facing_up: **EXAMPLE:**

```python
tupla_1 = (1,2,'hola')
print(tupla_1)
print('Tercer elemento de la tupla es:', tupla_1[2])
```

>:mega: **NOTA:**
>
>* ("hola",) --> es una tupla con un solo elemento
>* ("hola) --> es un string (python no lo reconoce como tupla)
>```python
># Esto es una tupla con un elemento
>tupla_1_elem = ('Hola',)
>print(tupla_1_elem)
>print(tupla_1_elem[0])
># Esto es un string
>string_var = ('Hola')
>print(string_var)
>print(string_var[0])
>```

>:mega: **NOTA:**
>
> Para ver si una tupla contiene un elemento:
>```python
>tupla_1 = (1,2,3,4,5)
># Para ver si un elemento se encuentra en una tupla
>print(2 in tupla_1) # --> True
>```

>:mega: **NOTA:**
>
> Para convertir una lista en tupla:
>```python
>list_1 = [1,2,3,4,5]
>tuple_1 = tuple(list_1)
>```

### 2.3.1 Access elements (equal for lists)

```python
# Devolver el element 2 de la tupla
el = tupla_1(1)

# Devolver último y penúltimo elemento de la tupla
tupla_1(-1) # -1 = N
tupla_1(-2) # -2 == N-1

# Devoler tupla con primeros 4 elementos
tupla_1(:4)# :4 = 0:3

# Devoler tupla con elementos del 4 hasta N
tupla_1(4:)# 4: = 4:N

# Devolver tupla con 3 últimos elementos
tupla_1(-3:) # -3: = N-3:N

# Devoler tupla con elementos hasta N-2
tupla_1(:-2)# :-2 = 0:N-2
```

### 2.3.2 Methods

* Indicar el numero de veces que aparece un elemento

```python
tuple_1.count()
```

* Busca la posicion que ocupa un determinado elemento en la tupla

```python
tuple_1.index()
```

* Longitud de la tupla

```python
len(tuple_1)
```

### 2.4 Lists

Secuencias ordenadas de datos modificables (se pueden modificar y añadir datos).

* Es posible la mezcla de tipos de datos

### 2.4.1 Access Elements

```python
# Devolver el element 2 de la lista
el = lista_1[1]

# Devolver último y penúltimo elemento de la lista
lista_1[-1] # -1 = N
lista_1[-2] # -2 == N-1

# Devoler lista con primeros 4 elementos
lista_1[:4]# :4 = 0:3

# Devoler lista con elementos del 4 hasta N
lista_1[4:]# 4: = 4:N

# Devolver lista con 3 últimos elementos
lista_1[-3:] # -3: = N-3:N

# Devoler lista con elementos hasta N-2
lista_1[:-2]# :-2 = 0:N-2
```

### 2.4.2 Methods

* Obtener un elemento de una lista:

```python
# Obtain elem in pos 1 of a list
list[1]
```

* Add element to the end of a list:

```python
lista_1.append(34)
lista_1.append('suuuu')
```

* Add element to a concrete position of a list

```python
# Add element 3 in pos 1
lista_1.insert(3,1)
```

* Eliminar todas las apariciones de un elemento en la lista

```python
lista_1.remove('suuuu')
lista_1.remove(1)
```

* ELiminar un elemento de una pos concreta de la lista y devolverlo

```python
elem = lista_1.pop()
```

* Ordenar lista

```python
lista_1.sort()
```

* Vaciar lista

```python
lista_1.clear()
```

### 2.5 Dictionaries

Colecciones no ordenadas de valores, modificables, donde cada valor va asociado a una clave.

```python
dic = {'nombre':'Claudia', 
       'DNI' : 43378901,
       'pesos' : [15,15,16,17,16,18,19]}

# Obtener elementos del diccionario
print(dic.get('DNI'))
print(dic['DNI'])
print(dic.get('pesos')[2])

# Modificar / añadir elementos del diccionario
dic['tiempo'] = [35,36,38,32,31]
print(dic)
dic['nombre'] = 'Alex'
print(dic)

print('\n','='*6,'\n')
# Si iteramos un diccionario obtenemos las claves!
for elem in dic:
  print(elem,':',dic[elem])

print('\n','='*6,'\n')
# Otra forma de iterar
for key, val in dic.items():
  print(key,':',val)

# dic.items() nos devuelve una lista con tuplas dentro
print('\n','======','\n')
print(dic.items())
```

### 2.6 Strings

No son más que listas de caracteres

```python
name = "Alejandro Campos. El fucking boss"
print(name[-3:])
```

### 2.6.1 Methods

* Mayus / Minus:

```python
# Mayusculas
print(name.upper())
print(name) # Este no estará en mayusculas
# Minuscula
print(name.lower())
```
* Mayuscula al principio de cada palabra:

```python
nameCap = name.capitalize()
```

* Quitar espacios:

```python
# Quitar espacios por delante y por detras
print(name.strip())

# Quitar espacios solo por delante
print(name.rstrip())

# Quitar espacios solo por detras
print(name.lstrip())
```

* Mas metodos de strings:

```python
# Devuelve una tupla con las palabras que hay
print(name.split())

# Devuelve una tupla con las palabras que hay separadas por un .
print(name.split('.'))
print(name)

# Devulve primera posicion donde se encuentra a
print(name.index('a'))
```

## 3. Operators

### 3.1 Mathematic

```python
# Suma Resta ya lo sabes --> Easy

# División
print(16/3)

# División entera
print(16//3)
print(16.5//3)

# Residuo
print(16%3)
print(16.5%3)

# Elevación
print(2**2)
print(2**3)
print(2**10)
```

### 3.2 Logic

* is, ==
* is not, !=
* or
* and
* in --> si está contenido en tupla, lista, diccionario (clave)...

### 3.3 Concatenated

Solamente admite dos tipos iguales de datos, podemos sumar dos ints o dos strings pero nunca un int y un string

* A + B = AB
* A * 3 = AAA

Para convertir un string a int --> int(string_x) como veremos en los metodos de conversion

## 4. Metodos por defecto en Python

### 4.1 Metodos de conversion
Necesarios para convertir un tipo de datos a otro tipo de datos

* convertir a string: str()
* convertir a int: int()
* convertir a float: float()
* convertir a bool: bool()
* convertir a lista: list()

### 4.2 Interacción con terminal

* print: escribe en la stdout (salida estandar)
* input: recoge datos de la entrada de teclado

:page_facing_up: **EXAMPLE:**

```python
print("Hola como estás")
edad = input('Que edad tienes?')
print(int(edad)+1)
```

## 5. Controladores de flujo

Van sin parentesis

* if
* else
* elif

:page_facing_up: **EXAMPLE:**

```python
# Ejemplo de controladores de flujo
edad = int(input('Que edad tienes?'))
if edad < 18:
  print('Lo sentimos mucho, pero al ser menor de edad no podemos mostrarte el contenido')
elif edad > 65:
  print('Lo sentimos mucho, eres demasiado mayor para poder ver el contenido')
else:
  print('69')
```

>:mega: **NOTA:**
>
>If / else en una linea
>```python
>os = 'windows' if platform.system().lower() == 'windows' else 'linux'
>```

## 6. Loops

### 6.1 For Loop

```python
# Por elementos en lista / tupla / diccionario
c = {'nombre':'Claudia', 
       'DNI' : 43378901,
       'pesos' : [15,15,16,17,16,18,19]}

## Te pintará las claves
for elem in c:
  print(elem)

# Por indices
lista = [1,3,5,7,9,13,18]

## Te itereará hasta el final de la lista
for i in range(len(lista)):
  print(lista[i])

## Te itereará hasta el final de la lista -3 elementos
for i in range(3,len(lista)-3):
  print(lista[i])

## Te itereará hasta el final de la lista de 2 en 2 elementos
for i in range(1,len(lista),2):
  print(lista[i])
```

>:mega: **NOTA:**
>
>El bucle for puede pararse en cualquier momento con la orden **break**

### 6.2 While Loop

```python
i = 0
while True:
  print("Hola")
  i+=1
  if i > 5:
    break
```

## 7. Methods (def)

```python
def saludo(name='', exclamacion=False):
  if exclamacion:
    print("Hi broo",name,"!!!")
  else:
    print('Hi bro',name)

saludo('Claudia',True)
saludo('Alex')
saludo()
```

>:mega: **NOTA:**
>
>```python
> from typing_extensions import ParamSpecArgs
> # Para dejar un metodo vacio
> def saludo_3():
>  pass
>```

## 8. Imports
Para importar metodos de otros modulos en el mismo directorio

```python
# Modulos publicos
from time import sleep
# Modulos locales
  ## Siendo menu.py el modulo en el mismo directorio
from menu import method
```

Los imports se organizan siempre de la siguiente manera

1. Imports de librerias externas en orden alfabetico
2. Imports de librerias internas en orden alfabetico

## 9. Python Object Oriented

### 9.1 Object Definition
Python puede usarse para programar orientado a objetos. Los objetos nos ayudan a que el codigo sea mucho más limpio y ordenado, teniendo los atributos / variables ordenadas por clases / obejtos.

**Notas:**
* Las clases comienzan siempre por mayuscula
* Las clases heredan de java y utilizan la nomenclatura CamelCase = PrimerasLetrasMayusculas
* No es tan rígido como java, pueden declararse las clases / subclases en diferentes ficheros, no tiene que haber un fichero por clase
* Se suelen definir todas las clases / subclases relacionadas con un mismo tema en un mismo fichero

**Important**
* El self debe irse arrastrando por los metodos que se contengan en la clase

### 9.2 Constructor

```python
# Definimos la clase Prueba
class Prueba:
  # Definimos su constructor
  def __init__(self, name, timeout = 200):
    self.name = name
    self. timeout = timeout
```

Ejemplo --> Servicio web en directorios

### 9.3 Class Instantiation

```python
tst = Prueba("Prueba1", 300)
```

### 9.4 Atributes

Los atributos se definen previamente al constructor

```python
# Definimos la clase Prueba
class Prueba:

  # Definimos atributos
  stop_count = False

  # Definimos su constructor
  def __init__(self, name, timeout = 200):
    self.name = name
    self. timeout = timeout
```

Pueden ser editados a nivel de instancia, modificando tan solo el contenido del atributo para una instancia en concreto.

```python
tst = Prueba("Prueba1", 300)
tst.stop_count = True
tst.name = "Prueba_Fake"
```

Pero pueden ser también modificados a nivel de clase, cambiando el valor para todos los objetos de la misma clase.

```python
tst = Prueba("Prueba1", 300)
tst_2 = Prueba("Prueba2", 400)
Prueba.stop_count = True
```

### 9.5 Methods

To define methods into a class:

```python
# Definimos la clase Prueba
class Prueba:

  # Definimos su constructor
  def __init__(self, ...):
    pass

  # Defining saluda method
  def saluda():
    print("Hello")
```
#### 9.5.1 Class Methods

Para definir metodos que puedan usarse a nivel de clase, es decir que puedan llamarse sin instanciarse.

```python
# Definimos la clase Prueba
class Prueba:

  # Atribute
  stop_count = False

  # Definimos su constructor
  def __init__(self, ...):
    pass

  # Aquí definimos una nueva función a nivel de clase
  # Parará todos los timers de todos los objetos de la clase Prueba, porque es Timer.stop_count y no self.stop_count...
  @classmethod
  def stopAll(cls):
    Timer.stop_count_class = True
```

### 9.6 Inheritance
```python
# Definimos una clase PruebaServicio que extiende Prueba (hereda) y utiliza una instancia servicio para funcionar
class PruebaServicio(Prueba):
  def __init__(self, name, timeout, servicio, metodo, respuestas):
    super().__init__(name, timeout)
    self.servicio = servicio
    self.metodo = metodo
    self.respuestas = respuestas
```


## 10. Threads

## 11. Yaml read

## 12. Bash with python

## 13. Examples

## 14. TODO:

- [] Pool de hilos
- [] Devolver objetos 
- [] Modificar como se muestra un objeto cuando se convierte a string
- [] Modificar como se muestra un objeto dentro de una tupla, lista o diccionario
- [] TestsCases
- [] Tratado de diccionarios con .keys() o .values() que devuelve listas
- [] Excepciones
- [] Lenguajes de marcado --> YAML, JSON, XML, HTML, CSV, Markdown
  - [] De consulta: SQL
  - [] De modelado: UML
- [] Lectura de yaml --> Se pueden transformar facilmente a diccionario

