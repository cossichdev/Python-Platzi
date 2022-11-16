import unittest  # importar modulo de python que permite generar pruebas, y genera pruebas...

def suma (num1, num2):
    return num1 + num2
class CajaNegraTest(unittest.TestCase): #...generando una clase, un caso de prueba

    def test_suma(self): #generar caso de prueba
        num1 = 10
        num2 = 5

        resultado = suma(num1, num2) #resultado de una suma nos de un valor

        self.assertEqual(resultado, 15)  #asegurarnos que nuestro resultado sea correcto usamos el assert
        
    def test_neg(self):
        num1 = -10
        num2 =  -7
        
        resultado = suma(num1, num2)
        
        self.assertEqual(resultado, -17)

if __name__ == '__main__': #para correr el test, tenemos que definir que este es el modulo principal, por eso agregamos el if name, main y agregamos el unitttest
    unittest.main()