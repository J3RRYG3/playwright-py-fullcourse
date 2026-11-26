name = 'Gerardo'

# Slicing
print(name[:2])
print(name[:])
print(name[:-4])
print(name[-1])
#reverse string 
'''
En Python, [::-1] usa el operador de slicing:

inicio : fin : paso
:: indica que no se especifican inicio ni fin.
-1 es el paso; significa recorrer hacia atrás.
'''
print(name[::-1])
print("-------")
print(name[::-2])
print(len(name))


'''strip method removes leading and
trailing whitespace from a string. 
It can also remove specified characters from the beginning and end of the string.
'''
print("removing blank spaces from a string at the beginning and end")

#removing blank spaces from a string at the beginning and end
name_with_spaces = '   Gerardo   '
print(name_with_spaces.strip())

#removing blank spaces from a string at the right
name_with_spaces = '   Gerardo   '
print(name_with_spaces.rstrip())
#removing blank spaces from a string at the left
name_with_spaces = '   Gerardo   '
print(name_with_spaces.lstrip())  
#removing the dot 
name_with_dot = 'Gerardo.'
print(name_with_dot.rstrip('.'))

'''upper() and lower() methods are used to convert the case of a string.'''
print("Converting the case of a string")
name = 'Gerardo'
print(name.upper())
print(name.lower())

'''split() method is used to split a string into a list of substrings based on a specified delimiter.'''

print("Splitting a string into a list of substrings")
name = 'Gerardo Lopez'
print(name.split())
email = 'gerardo.mejiamg@gmail.com'
print(email.split('@'))
print(email.split('.'))
print(email.split('@')[0])   # Get the username part
print(email.split('@')[1])   # Get the domain part
print(email.split('.')[0])   # Get the first part of the domain
print(email.split('.')[1])   # Get the second part of the domain
print(email.split('.')[2])   # Get the third part of the domain

