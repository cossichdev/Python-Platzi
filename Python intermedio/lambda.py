
#  high order functions:  filter 

# my_list = [1, 4, 5, 6, 9, 13, 19, 21]
# odd = [i for i in my_list if i % 2 != 0]

# print(odd)


# my_list = [1, 4, 5, 6, 9, 13, 19, 21]
# odd = list(filter(lambda x: x % 2 != 0, my_list))

# print(odd)


#  high order functions:  map

# my_list = [1, 2, 3, 4, 5]
# squares = [i**2 for i in my_list]

# print(squares)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# odd = list(map(lambda x: x ** 2, my_list))

# print(odd)



#  high order functions:  reduce

# my_list = [2, 2, 2, 2, 2]
# all_multiplied = 1

# for i in my_list:
#     all_multiplied = all_multiplied * i

# print(all_multiplied)


from functools import reduce
my_list = [2, 2, 2, 2, 2]

all_multiplied = reduce(lambda a,b: a * b, my_list)

print(all_multiplied)