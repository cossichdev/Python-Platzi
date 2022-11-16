import unittest


def mayoredad(edad):  # generar caso de prueba
    if edad >= 18:
        return True
    else:
        return False

class CajaCristalTest(unittest.TestCase):  # ...generando una clase, un caso de prueba, se escribe a continuación el test

    def testmayor(self):
        edad = 20

        resultado = mayoredad(edad)

        self.assertEqual(resultado, True)

    def testmenor(self):
        edad = 19

        resultado = mayoredad(edad)

        self.assertEqual(resultado, False) #respuesta que deberia de dar la definicion creada



if __name__ == '__main__':  # para correr el test, tenemos que definir que este es el modulo principal, por eso agregamos el if name, main y agregamos el unitttest
    unittest.main(verbosity=2)
