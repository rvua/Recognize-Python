num1 = 42 # variable declaration, Data Type: Numbers
num2 = 2.3 # variable declaration, Data Type: Float
boolean = True # variable declaration, Data Type: Boolean
string = 'Hello World' # variable declaration, Data Type: String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, Data Type: Initialize List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration. Data Type: Initialize Dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, Data Type: Initialize Tuple 
print(type(fruit)) # log statement, Type Check -- Tuple
print(pizza_toppings[1]) # log statement, List: Access Value 
pizza_toppings.append('Mushrooms') # List: Add Value
print(person['name']) # log statement, Dictionary: Access Value 
person['name'] = 'George' # Dictionary: Change Value
person['eye_color'] = 'blue' # Dictionary: Change Value
print(fruit[2]) # log statement, Tuple: Access Value

if num1 > 45: # conditional: if statement, evaluation
    print("It's greater") # log statement 
else: # conditional: else statement
    print("It's lower") # log statement

if len(string) < 5: # conditional: if statement
    print("It's a short word!") # log statement
elif len(string) > 15: # conditional: elif statement
    print("It's a long word!") # log statement
else: # conditional: else statement
    print("Just right!") # log statement

for x in range(5): # for-loop: start at 0, go up and stop at 5 
    print(x) # log statement 
for x in range(2,5): # for-loop: start at 2, go up and stop at 5 
    print(x) # log statement 
for x in range(2,10,3): # for-loop: start at 2, goes up to until 10, increments by 3
    print(x) # log statement
x = 0 # variable declaration
while(x < 5): # while-loop: stop at 5
    print(x) # log statement
    x += 1 # increment: x by 1 until loop stops. 

pizza_toppings.pop() # List: Delete Value at end
pizza_toppings.pop(1) # List: Delete Value at index

print(person) # log statement to console of dictionary
person.pop('eye_color') # Dictionary: Delete Value
print(person) # log statement to console of dictionary

for topping in pizza_toppings: # for-loop: Through a list
    if topping == 'Pepperoni': # conditional: if statement
        continue # for-loop: continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional: if statement
        break # for-loop: break, stops the loop

def print_hello_ten_times(): # function declaration
    for num in range(10): # for-loop: starts at 0, goes up until 10
        print('Hello') # log statement

print_hello_ten_times() # function call

def print_hello_x_times(x): # function declaration: with paramenter: x
    for num in range(x): # for-loop: up until a given number x
        print('Hello') # log statement

print_hello_x_times(4) # function call, argument: 4

def print_hello_x_or_ten_times(x = 10): # function declaration, default paramenter: x = 10
    for num in range(x): # for-loop: until x
        print('Hello') # log statement

print_hello_x_or_ten_times() # function call: goes to 10
print_hello_x_or_ten_times(4) # function call, arguement: 4. goes to 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)