#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

print("Enunciado--------------------")

#Insert here the module/library import statements 
import math
import os
import random
import numpy as np


#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

print("Ejercicio1 ------------------")
square = [i**2 for i in range(20) ]
print(square)
print("------------------")

#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

print("Ejercicio2 ------------------")
power_of_two = [2**i for i in range(50) ]
print(power_of_two)
print("------------------")

#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

print("Ejercicio3 ------------------")
sqrt = [math.sqrt(i) for i in range(100) ]
print( sqrt)
print("------------------")


#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

print("Ejercicio4 ------------------")
my_list = [i for i in range(-10,1) ]
print( my_list)
print("------------------")


#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

print("Ejercicio5 ------------------")
odds = [i for i in range(1,100,2) ]
print( odds)
print("------------------")


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

print("Ejercicio6 ------------------")
divisible_by_seven = [i for i in range(1000) if i%7 == 0 ]
print( divisible_by_seven)
print("------------------")

#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

print("Ejercicio7 ------------------")

teststring = 'Find all of the words in a string that are monosyllabic'

def nn_vwls(x):
    vowels = ["a","e","i","o","u"]
    return [i for i in x if i not in vowels]
    

print(nn_vwls(teststring))

print("------------------")


#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

print("Ejercicio8 ------------------")
test_capital_letters = 'The Quick Brown Fox Jumped Over The Lazy Dog'

def capital_letters(x):
    return [i for i  in x if i.isupper()]

print(capital_letters(test_capital_letters))


print("------------------")

#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

print("Ejercicio9------------------")
test_consonants = 'The Quick Brown Fox Jumped Over The Lazy Dog'

def consonants(x):
    vowels = ["a","e","i","o","u"]
    return [i for i  in x if i not in vowels and i is not " "]

print(consonants(test_consonants))


print("------------------")


#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

print("Ejercicio10------------------")

files  = os.listdir()
print(files)

print("------------------")


#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

print("Ejercicio11------------------")

def random_lists():
    return [random.sample(range(100), 10) for i in range(4)]
    
print(random_lists())

print("------------------")


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

print("Ejercicio12------------------")

def flatten_list(x):
    return [z for i in x for z in i]

print(flatten_list(list_of_lists))

print("------------------")


#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

print("Ejercicio13------------------")

def floats(x):
    return [float(z) for i in x for z in i]

print(floats(list_of_lists))

print("------------------")



#14. Handle the exception thrown by the code below by using try and except blocks. 

print("Ejercicio14------------------")

for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        raise Exception((i,"no es una string por lo que no puede elevarse"))

print("------------------")


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

print("Ejercicio15------------------")

x = 5
y = 0

try:
    z = x/y
except:
    print(('no es posible dividir un numero entre 0'))

finally:
    print("All Done")
print("------------------")
 

#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
print("Ejercicio16------------------")
abc=[10,20,20]
try:
    print(abc[3])
except:
    raise TypeError("Argumento fuera del rango de la lista")
print("------------------")

#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

print("Ejercicio17------------------")

numarator = input("Please, enter the numerator\n:")
denominator = input("Please, enter the denominator\n:")

def divide(a,b):
    if type(a) != int or type(a) != float:
        try:
            a = float(a)
        except:
            raise TypeError(f"a no es compatible, debe ser un entero o float y es del tipo {type(a)}")
    if type(b) != int or type(b) != float:
        try:
            b = float(b)
        except:
            raise TypeError(f"b no es compatible, debe ser un entero o float y es del tipo {type(b)}")
    if b == 0:
        raise ZeroDivisionError("b no puede ser 0")
        
    return a / b
    
       
print(divide(numarator,denominator))

print("------------------")


#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
print("Ejercicio18------------------")

try:
    f = open('testfile','r')
    f.write('Test write this')
except:
        raise Exception(TypeError(),"Fichero no encontrado")




print("------------------")

#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

'''
print("Ejercicio19------------------")

def fichero():
    try:
        fp = open('myfile.txt')
        line = f.readline()
    except:
        if TypeError is FileNotFoundError:
            print(TypeError("Fichero no encontrado") 
            

def tipo():
    try:
        i = int(s.strip())
    except:
        if TypeError is TypeError:
            print(TypeError("Fichero no encontrado")
        raise TypeError()

print("------------------")   
'''
#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

print("Ejercicio20------------------")
def linux_interaction():
    try:
        assert ('linux' in sys.platform), "Function can only run on Linux systems."
    except:
        return "You are using MAC OS!"
    finally:
        return('Doing something.')

print(linux_interaction())
print("------------------")

# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.


print("Ejercicio21------------------")       
def cuadrado():
    while True:
        try:
            numero = int(input("Introduce un número entero,porfa\n"))
        except ValueError:
            print("Tío, eso no es un número")
            continue
        else:
            break
    return numero**2
    

print(cuadrado())
print("------------------")

# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 
print("Ejercicio22------------------")  
def results():
   return set([i for i in range(1,1001) for r in range(2,9) if i % r == 0])
    
print(results())

print("------------------")

# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python
'''
class ThisIsNotIntegerError:
    print("Esto no es un número")


    def cuadrado():
        while True:
            try:
                Total_Marks = int(input("Enter Total Marks Scored: "))
            except:
                raise ThisIsNotIntegerError
                continue
            else:
                break
        return Total_Marks
 

print(cuadrado()) 

Num_of_Sections = int(input("Enter Num of Sections: "))
'''