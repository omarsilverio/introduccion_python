#https://docs.python.org/es/3/tutorial/controlflow.html

#LA SENTENCIA IF
numero = int(input("por favor introduzca un numero:\n"))

if numero < 0:
    numero = 0
    print('valor negativo resetado a 0')
elif numero == 0:
    print('es cero')
elif numero == 1:
    print('es el uno')
else:
    print('el numero es mayor a uno')

#LA SENTENCIA FOR
#La sentencia for en Python difiere un poco de lo que uno puede 
#estar acostumbrado en lenguajes como C o Pascal. 
#En lugar de siempre iterar sobre una progresión aritmética de números 
#(como en Pascal) o darle al usuario la posibilidad de definir tanto el 
#paso de la iteración como la condición de fin (como en C), la sentencia 
#for de Python itera sobre los ítems de cualquier secuencia (una lista o una cadena de texto), 
#en el orden que aparecen en la secuencia.

words = ['cat','window','defenestrate']
for word in words:
    print(word, len(word))

#Código que modifica una colección mientras se itera sobre la misma colección puede ser complejo 
#de hacer bien. Sin embargo, suele ser más directo iterar sobre una copia de la colección o crear 
#una nueva colección:
# Elimina un elmento del arreglko original
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# crea un nuevo arregñlo con los elementos dados
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(users)
print(active_users)

#Si se necesita iterar sobre una secuencia de números, es apropiado utilizar la función integrada range(), la cual genera progresiones aritméticas:
for i in range(5):
    print(i)

#El valor final dado nunca es parte de la secuencia; 
#range(10) genera 10 valores, los índices correspondientes para los ítems de 
#una secuencia de longitud 10. Es posible hacer que el rango empiece con otro número, 
#o especificar un incremento diferente (incluso negativo; algunas veces se lo llama “paso”):
print(list(range(5, 10)))

print(list(range(0, 10, 3)))

print(list(range(-10, -100, -30)))

#Para iterar sobre los índices de una secuencia, puedes combinar range() y len() así:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#Algo extraño sucede si tan sólo muestras un range:
print(range(10))

#El objeto retornado por range() se comporta de muchas maneras como si fuera una lista, 
#pero no lo es. Es un objeto que retorna los ítems sucesivos de la secuencia deseada 
#cuando iteras sobre él, pero realmente no construye la lista, ahorrando entonces espacio.
print(sum(range(4)))  # 0 + 1 + 2 + 3

#BREAK AND CONTINUE STATEMENTS
#a instrucción se sale del FOR o WHILE más interno:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
#La declaración continue con lo siguiente Iteración del bucle:
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

#Clauses on Loopselse
#En un bucle for o while, la instrucción puede ir acompañada de una cláusula else. 
#Si el bucle termina sin ejecutar un break, se ejecuta la cláusula else.
#En un bucle for, la cláusula else se ejecuta después de que el bucle finaliza su última iteración, 
#es decir, si no ocurrió un break.
#En un bucle while, se ejecuta después de que la condición del bucle se vuelva falsa.
#En cualquier tipo de bucle, la cláusula else no se ejecuta si el bucle fue terminado 
#por un break. Por supuesto, otras formas de finalizar el bucle prematuramente, 
#como un return o una excepción lanzada, también omitirán la ejecución de la cláusula else.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

#la sentencia match
#Una sentencia match recibe una expresión y compara su valor con patrones 
#sucesivos dados en uno o más bloques case. Esto es similar a grandes rasgos 
#con una sentencia switch en C, Java o JavaScript (y muchos otros lenguajes) 
#pero es más similar a la comparación de patrones en lenguajes como Rust o Haskell. 
#Sólo se ejecuta el primer patrón que coincide y también es capaz de extraer componentes 
#(elementos de una secuencia o atributos de un objeto) de un valor y ponerlos en variables.

#Se pueden combinar varios literales en un solo patrón usando («o»):|


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"

print(http_error(401))

#¡Observa éste caso con cuidado! El primer patrón tiene dos literales y 
#puede considerarse una extensión del patrón literal que se mostró anteriormente. 
#Pero los siguientes dos patrones combinan un literal y una variable, y la variable 
#liga uno de los elementos del sujeto (). El cuarto patrón captura ambos elementos, 
#lo que lo hace conceptualmente similar a la asignación que desempaqueta .point(x, y) = point

# point is an (x, y) tuple
point = (1,1)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
#Si estás usando clases para estructurar tus datos, 
#puedes usar el nombre de la clase seguida de una lista de argumentos similar a la de un constructor, 
#pero con la capacidad de capturar atributos en variables:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point_object = Point(0,0)

def where_is(point_object):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

points = [Point(0,0)]
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

#LA SENTENCIA PASS
#La sentencia pass no hace nada. 
#Se puede usar cuando una sentencia es requerida por la sintaxis pero el programa no 
#requiere ninguna acción. Por ejemplo:
#while True:
    #pass  # Busy-wait for keyboard interrupt (Ctrl+C)

#Se usa normalmente para crear clases en su mínima expresión:
class MyEmptyClass:
    pass

#Otro lugar donde se puede usar pass es como una marca de 
#lugar para una función o un cuerpo condicional cuando estás trabajando en código nuevo, 
#lo cual te permite pensar a un nivel de abstracción mayor. El se ignora silenciosamente:pass
def initlog(*args):
    pass   # Remember to implement this!


#Definir funciones
def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

#La palabra reservada def se usa para definir funciones. 
#Debe seguirle el nombre de la función y la lista de parámetros formales entre paréntesis. 
#Las sentencias que forman el cuerpo de la función empiezan en la línea siguiente, 
#y deben estar con sangría.