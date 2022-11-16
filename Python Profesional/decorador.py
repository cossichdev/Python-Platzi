from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time =datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range (1, 1000000):
        pass
random_func()

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre="Cesar"):
    print("hola" + nombre)

random_func()
suma (5, 5)
saludo ("Glauco")
