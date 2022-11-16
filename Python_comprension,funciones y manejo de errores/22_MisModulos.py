#Todo archivo con terminacion ".py" pouede actuar como modulo, dentro de un modulo se pueden definis clases, variables o funciones.
#ver carpeta creada llamada "APP"


#Tamnbien podemos importar un paquete (carpeta pkg) una parte del codigo
from pkg.mod1 import fun1, fun2
from pkg.mod2 import fun3, fun4

print(fun1())
print(fun2())
print(fun3())
print(fun4())

import pkg
print(pkg.url) #variable de archivo __init__.py
print(pkg.mod1.fun1()) #funcion de archivo mod1.py pero puede causar errores si no se importan bien los modulos
print(pkg.mod2.fun3()) #funcion de archivo mod2.py pero puede causar errores si no se importan bien los modulos