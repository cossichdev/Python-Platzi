set_colors1 = {'blue', 'red', 'green', 'yellow', 'orange', 'purple', 'black', 'white', 'gray', 'brown', 'pink', 'violet', 'indigo', 'gold', 'silver', 'bronze', 'black', 'white', 'gray', 'brown', 'pink', 'violet', 'indigo', 'gold', 'silver', 'bronze'}
set_colors2 = {'blue', 'red', 'green', 'gold', 'silver', 'bronze'}

set_numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
set_numbers2 = {1, 2, 3, 4, 5, 6, 7, 8,}


set_countries1 = {'Colombia', 'Peru', 'Chile', 'Argentina', 'Bolivia', 'Ecuador', 'Venezuela'} 
set_countries2 = {'Venezuela', 'Brasil', 'Paraguay', 'Uruguay', 'Colombia', 'Peru', 'Chile', 'Argentina', 'Bolivia', 'Ecuador', 'Venezuela', 'Brasil', 'Paraguay', 'Uruguay'}

#las operaciones entre conjuntos son similares a las operaciones entre conjuntos matemáticos y se pueden realizar con los operadores &, |, -, ^, <=, >=, <, >, ==, !=

#union
unionSet = set_colors1 | set_numbers1 | set_countries1 #operador | para unión de conjuntos (también se puede usar el método union)
print(unionSet)

#intersection
intersecSet = set_colors1 & set_colors2 #operador & para intersección de conjuntos, devuelve los elementos que se encuentran en ambos conjuntos
print(intersecSet)

#difference
diferenSet = set_numbers1 - set_numbers2 #operador - para diferencia de conjuntos, devuelve los elementos que están en el primer conjunto y no están en el segundo conjunto
print(diferenSet)

#symmetric difference
simetrSet = set_countries1 ^ set_countries2 #operador ^ para diferencia simétrica de conjuntos, es decir, los elementos que están en un conjunto o en el otro pero no en ambos
print(simetrSet)