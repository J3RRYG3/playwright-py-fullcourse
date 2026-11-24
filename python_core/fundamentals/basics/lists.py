my_list = ["string",10,3.1,True, [1,2,3]]#no es ideal utlizar listas heterogeneas.
print(type(my_list))

#listas homogeneas
courses = ["C#", "java", "python", "js", "ts", "rust"]
numbers = [2,4,5,6]

print (courses)
print (numbers)

# imprimiendo elementos por indices
print(courses[1])

# imprimiendo elementos cuando no conocemos cuantos elementos son:
#con esto sabemos el numero total de elementos
print(len(courses))
#conocer el ultimo indice de la lista
last_index = len(courses) -1

#mostrar el ultimo elemento de la lista
value = courses[-1]
print(value)
#mostrar el penultimo elemento
value = courses[-2]
print(value)

# mostrar todos los elementos de la lista
value = courses[:]
print(value)

# mostrar los elementos de la lista menos el ultimo elemento
value = courses[:-1]
print(value)

#acutalizar lista
courses[0] = "python"
courses[2] = "golang"
print(courses[:])

'''Sublistas - Slicing'''
#creando sublista
# new_list = [
#     courses[0],
#     courses[3],
#     courses[5]
# ]

#forma mejorada
new_list = courses[0:3]
print(new_list)

#creando lista con los ultimos elementos de la lista original
new_list2 = courses[3:5]
print(new_list2)

#creando nueva lista con saltos de elementos de 2 en 2
new_list3 = courses[::2]
print(new_list3)

#invirtiendo list
invert_list = courses[::-1]
print(invert_list)