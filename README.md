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
print(2 in tupla_1) # --> True
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

## 3. Mathematic Operators

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

