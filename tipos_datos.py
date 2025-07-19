# this is the first comment https://docs.python.org/es/3/tutorial/introduction.html
#https://docs.python.org/es/3/library/stdtypes.html#numeric-types-int-float-complex

spam = 1  # and this is the second comment
    # ... and now a third!
text = "# This is not a comment because it's inside quotes."

#NUMEROS
# puedes introducir una expresión en él y este escribirá los valores. 
#La sintaxis es sencilla: los operadores +, -, * y / se pueden usar para realizar operaciones aritméticas; 
#los paréntesis (()) pueden ser usados para agrupar

print(2 + 2)
print(50 - 5*6)
print((50 - 5*6) / 4)
print(8 / 5)  # division always returns a floating-point number

#Los números enteros (ej. 2, 4, 20) tienen tipo int, 
#los que tienen una parte fraccionaria (por ejemplo 5.0, 1.6) tiene el tipo float.

#La división (/) siempre retorna un número decimal de punto flotante. 
#Para hacer floor division y obtener un número entero como resultado puede usarse el operador //; 
#para calcular el resto puedes usar %

print(17 / 3) # classic division returns a float
print(17 // 3) # floor division discards the fractional part
print(17 % 3) # the % operator returns the remainder of the division
print(5 * 3 + 2)  # floored quotient * divisor + remainder

#Con Python, es posible usar el operador ** para calcular potencias
print(5 ** 2)
print(2 ** 7)

#El signo igual (=) se usa para asignar un valor a una variable.
#Si una variable no está «definida» (no se le ha asignado un valor), al intentar usarla dará un error:
width = 20
height = 5 * 9
print(width * height)

#Hay soporte completo de punto flotante; 
#operadores con operando mezclados convertirán los enteros a punto flotante:
print(4 * 3.75 - 1)

#Además de int y float, Python admite otros tipos de números, como Decimal y Fraction.
#Python también tiene soporte incorporado para complex numbers, 
#y usa el sufijo j o J para indicar la parte imaginaria (por ejemplo, 3+5j).

#TEXTO
#Python puede manipular texto (representado por el tipo str, conocido como «cadenas de caracteres») 
#al igual que números. Esto incluye caracteres «!», palabras «conejo», nombres «París», 
#oraciones «¡Te tengo a la vista!», etc. «Yay! :)». 
#Se pueden encerrar en comillas simples ('...') o comillas dobles ("...") con el mismo resultado

print('una sola comilla')
print("doble comillas")
print('1975') # digits and numerals enclosed in quotes are also strings

#Para citar una cita, debemos «escapar» la cita precediéndola con \. Alternativamente, podemos usar el otro tipo de comillas:
print('doesn\'t')  # use \' to escape the single quote...
print("doesn't")  # ...or use double quotes instead
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

#n el intérprete de Python, la definición de cadena y la cadena de salida pueden verse diferentes. 
#La función print() produce una salida más legible, omitiendo las comillas de encuadre e imprimiendo 
#caracteres escapados y especiales:
s = 'First line.\nSecond line.'  # \n means newline
print(s)

#Si no quieres que los caracteres precedidos por \ se interpreten como caracteres especiales, 
#puedes usar cadenas sin formato agregando una r antes de la primera comilla:
print('C:\some\name')
print(r'C:\some\name')  # note the r before the quote

#String literals can span multiple lines. 
#One way is using triple-quotes: """...""" or '''...'''. 
#End-of-line characters are automatically included in the string, 
#but it’s possible to prevent this by adding a \ at the end of the line. 
#In the following example, the initial newline is not included:
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#Las cadenas se pueden concatenar (pegar juntas) con el operador + y se pueden repetir con *:
# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')
#Dos o más cadenas literales 
#(es decir, las encerradas entre comillas) una al lado de la otra se concatenan automáticamente.
#Esta característica es particularmente útil cuando quieres dividir cadenas largas:
print('Py' 'thon')
#Esto solo funciona con dos literales, no con variables ni expresiones:

#Si quieres concatenar variables o una variable y un literal, usa +:
prefix = 'py'
print(prefix + 'thon')

#Las cadenas de texto se pueden indexar (subíndices), 
#el primer carácter de la cadena tiene el índice 0. 
#No hay un tipo de dato diferente para los caracteres;
# un carácter es simplemente una cadena de longitud uno:
word = 'hola'
print(word[0])
print(word[3])

#Los índices también pueden ser números negativos, para empezar a contar desde la derecha:
print(word[-1])
print(word[-4])
#Nótese que -0 es lo mismo que 0, los índice negativos comienzan desde -1.

#Además de los índices, las rebanadas (slicing) también están soportadas. 
#Mientras que la indexación se utiliza para obtener caracteres individuales, 
#rebanar te permite obtener una subcadena:
print(word[0:2]) # characters from position 0 (included) to 2 (excluded)
print(word[2:4]) # characters from position 2 (included) to 4 (excluded)

#Los índices de las rebanadas tienen valores por defecto útiles; 
#el valor por defecto para el primer índice es cero, el valor por 
#defecto para el segundo índice es la longitud de la cadena a rebanar.

print(word[:2]) # character from the beginning to position 2 (excluded)
print(word[3:]) # characters from position 3 (included) to the end
print(word[-2:]) # characters from the second-last (included) to the end

#Nótese cómo el inicio siempre se incluye y el final siempre se excluye. 
#Esto asegura que s[:i] + s[i:] siempre sea igual a s:
print(word[:2] + word[2:])
print(word[:4] + word[4:])

#Una forma de recordar cómo funcionan las rebanadas es pensar que los 
#índices apuntan entre caracteres, con el borde izquierdo del primer carácter numerado 0. 
#Luego, el punto derecho del último carácter de una cadena de n caracteres tiene un índice n, 
#por ejemplo:

#+---+---+---+---+---+---+
#| P | y | t | h | o | n |
#+---+---+---+---+---+---+
#0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

#La primera fila de números da la posición de los índices 0…6 en la cadena; 
#La segunda fila da los correspondientes indices negativos. 
#La rebanada desde i hasta j consta de todos los caracteres entre los bordes etiquetados i y j, 
#respectivamente.
#Para índices no negativos, la longitud de la rebanada es la diferencia de los índices, si ambos están dentro de los límites. Por ejemplo, la longitud de word[1:3] es 2.

#Intentar usar un índice que es muy grande resultará en un error:
#Sin embargo, los índices de rebanadas fuera de rango se 
#manejan satisfactoriamente cuando se usan para rebanar:
print(word[2:42])
print(word[:42])
#Las cadenas de Python no se pueden modificar, son immutable. Por eso, asignar a una posición indexada de la cadena resulta en un error:
#Si necesitas una cadena diferente, deberías crear una nueva:

print('J' + word[1:])
print(word[:2] + 'py')

#La función incorporada len() retorna la longitud de una cadena:
s = 'supercalifragilisticexpialidocious'
print(len(s))

#ver tambien
#https://docs.python.org/es/3/library/stdtypes.html#textseq
#https://docs.python.org/es/3/library/stdtypes.html#string-methods
#https://docs.python.org/es/3/reference/lexical_analysis.html#f-strings
#https://docs.python.org/es/3/library/string.html#formatstrings
#https://docs.python.org/es/3/library/stdtypes.html#old-string-formatting

#LISTAS
#Python tiene varios tipos de datos compuestos, 
#utilizados para agrupar otros valores. El más versátil es la lista, 
#la cual puede ser escrita como una lista de valores separados por coma (ítems) entre corchetes. 
#Las listas pueden contener ítems de diferentes tipos, pero usualmente los ítems son del mismo tipo.
squares = [1, 4, 9, 16, 25]
print(squares)
#Al igual que las cadenas (y todas las demás tipos integrados sequence), las listas se pueden indexar y segmentar:
print(squares[0])
print(squares[-1])
print(squares[-3:])
#Las listas también admiten operaciones como concatenación:
print(squares + [36, 49, 64, 81, 100])

#A diferencia de las cadenas, que son immutable, las listas son de tipo mutable, 
#es decir, es posible cambiar su contenido:
cubes = [1, 8, 27, 65, 125]
cubes[3] = 4 ** 3
print(cubes)

#tambien puede agregar un nuevo dato
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

#La asignación simple en Python nunca copia datos. 
#Al asignar una lista A una variable, la variable se refiere a la lista existente. 
#Se verá cualquier cambio que realice en la lista a través de una variable a través 
#de todas las demás variables que se refieren a él.:
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))  # they reference the same object
rgba.append("Alph")
print(rgb)

#Todas las operaciones de rebanado retornan una nueva lista que contiene los elementos pedidos. 
#Esto significa que la siguiente rebanada retorna una shallow copy de la lista:
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba)
print(rgba)

#También es posible asignar a una rebanada, 
#y esto incluso puede cambiar la longitud de la lista o vaciarla totalmente:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)

#La función predefinida len() también sirve para las listas
letters = ['a', 'b', 'c', 'd']
print(len(letters))

#Es posible anidar listas (crear listas que contengan otras listas), por ejemplo:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

#PRIMEROS PASOS A LA PROGRAMACION
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

#Este ejemplo introduce varias características nuevas.

#La primera línea contiene una asignación múltiple: las variables a y b obtienen simultáneamente los nuevos valores 0 y 1. En la última línea esto se usa nuevamente, demostrando que las expresiones de la derecha son evaluadas primero antes de que se realice cualquiera de las asignaciones. Las expresiones del lado derecho se evalúan de izquierda a derecha.

#El bucle while se ejecuta mientras la condición (aquí: a < 10) sea verdadera. En Python, como en C, cualquier valor entero que no sea cero es verdadero; cero es falso. La condición también puede ser una cadena de texto o una lista, de hecho, cualquier secuencia; cualquier cosa con una longitud distinta de cero es verdadera, las secuencias vacías son falsas. La prueba utilizada en el ejemplo es una comparación simple. Los operadores de comparación estándar se escriben igual que en C: < (menor que), > (mayor que), == (igual a), <= (menor que o igual a), >= (mayor que o igual a) y != (distinto a).

#El cuerpo del bucle está indentado: la indentación es la forma que usa Python para agrupar declaraciones. En el intérprete interactivo debes teclear un tabulador o espacio(s) para cada línea indentada. En la práctica vas a preparar entradas más complicadas para Python con un editor de texto; todos los editores de texto modernos tienen la facilidad de agregar la indentación automáticamente. Cuando se ingresa una instrucción compuesta de forma interactiva, se debe finalizar con una línea en blanco para indicar que está completa (ya que el analizador no puede adivinar cuando tecleaste la última línea). Nota que cada línea de un bloque básico debe estar sangrada de la misma forma.

#The print() function writes the value of the argument(s) it is given. It differs from just writing the expression you want to write (as we did earlier in the calculator examples) in the way it handles multiple arguments, floating-point quantities, and strings. Strings are printed without quotes, and a space is inserted between items, so you can format things nicely, like this:
i = 256*256
print('The value of i is', i)

#El parámetro nombrado end puede usarse para evitar el salto de linea al final de la salida, o terminar la salida con una cadena diferente:
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

#Debido a que ** tiene una prioridad mayor que -, -3**2 se interpretará como -(3**2), por lo tanto dará como resultado -9. Para evitar esto y obtener 9, puedes usar (-3)**2.
#A diferencia de otros lenguajes, caracteres especiales como \n tienen el mismo significado con simple('...') y dobles ("...") comillas. La única diferencia entre las dos es que dentro de las comillas simples no existe la necesidad de escapar " (pero tienes que escapar \') y viceversa.