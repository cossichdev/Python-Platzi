# a = [1,2,3,4,5,6,7,8]
# b = a
# c = [a , b]

# for element in c:
#     # print(element)


my_list = list(range(1, 101))

double = [i * 2 for i in my_list]
pares = [i for i in my_list if i % 2 == 0]

print(double, pares)