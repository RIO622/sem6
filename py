 Unit_1 Practical Assignment

1. Hello, World!

print("Hello, World!")

2. Add Two Numbers

# Input numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate sum
sum_result = num1 + num2

# Print result
print("The sum is:", sum_result)

3. Find the Square of a Number

# Input number
num = float(input("Enter a number: "))

# Calculate square
square = num ** 2

# Print result
print("The square of", num, "is", square)
4. Check if a Number is Even or Odd

# Input number
num = int(input("Enter a number: "))

# Check even or odd
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

5. Simple Interest Calculation
# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100
# Print result
print("The Simple Interest is:", simple_interest)

6. Calculate the Area of a Circle
import math
# Input radius
radius = float(input("Enter the radius of the circle: "))
# Calculate area
area = math.pi * radius ** 2
# Print result
print("The area of the circle is:", area)
7. Print Multiplication Table
# Input number
num = int(input("Enter a number: "))

# Generate multiplication table
print("Multiplication Table for", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
8. Find the Largest of Three Numbers
# Input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
# Find largest
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
9. Check if a String is a Palindrome
# Input string
text = input("Enter a string: ")
# Check palindrome
if text == text[::-1]:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
10. Factorial of a Number
# Input number
num = int(input("Enter a number: "))

# Calculate factorial
factorial = 1
for i in range(1, num + 1):
    factorial *= i

# Print result
print("The factorial of", num, "is", factorial)

1. Basic User Input

# Taking a simple user input
name = input("Enter your name: ")

# Printing a personalized greeting
print(f"Hello, {name}!")
Example Output:
Enter your name: Alice
Hello, Alice!	
2. User Input with Numbers
# Taking numerical input and performing a calculation
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Calculating the sum
sum_result = num1 + num2

# Displaying the result
print(f"The sum of {num1} and {num2} is {sum_result}.")
Example Output:
Enter the first number: 5
Enter the second number: 10
The sum of 5 and 10 is 15.
3. Evaluating Mathematical Expressions
# Taking a mathematical expression as input
expression = input("Enter a mathematical expression (e.g., 5 + 2 * 3): ")

# Evaluating the expression
result = eval(expression)

# Displaying the result
print(f"The result of the expression is: {result}")

Example Output:

Enter a mathematical expression (e.g., 5 + 2 * 3): 10 / 2 + 4
The result of the expression is: 9.0

4. Multiple Inputs in a Single Line

# Taking multiple inputs separated by spaces
inputs = input("Enter three numbers separated by spaces: ").split()

# Converting strings to integers
num1, num2, num3 = map(int, inputs)

# Calculating the average
average = (num1 + num2 + num3) / 3

# Displaying the result
print(f"The average of {num1}, {num2}, and {num3} is {average:.2f}.")

Example Output:

Enter three numbers separated by spaces: 4 8 12
The average of 4, 8, and 12 is 8.00.

5. Input Validation

# Taking input with validation
age = input("Enter your age: ")

if age.isdigit():
    print(f"Your age is {age}.")
else:
    print("Invalid input. Please enter a numeric value.")


Example Output:

Enter your age: twenty
Invalid input. Please enter a numeric value.
def check_numeric(x): if not isinstance(x, (int, float, complex)): raise ValueError('{0} is not numeric'.format(x))


6. Handling Floating-Point Input

# Taking floating-point input
radius = float(input("Enter the radius of a circle: "))

# Calculating the area
area = 3.14159 * radius ** 2

# Displaying the result
print(f"The area of the circle with radius {radius} is {area:.2f}.")

Example Output:

Enter the radius of a circle: 3.5
The area of the circle with radius 3.5 is 38.48.


7. Interactive User Input

# Asking the user a series of questions
name = input("What is your name? ")
age = input("How old are you? ")
hobby = input("What is your favorite hobby? ")

# Displaying a summary
print(f"\nSummary:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Hobby: {hobby}")
Example Output:

What is your name? Alice
How old are you? 25
What is your favorite hobby? Painting
Summary:
Name: Alice
Age: 25
Favorite Hobby: Painting
1. Assign and Print Integer Values
# Assigning integer values to variables
a = 10
b = 20

# Printing the values of the variables
print("Value of a:", a)
print("Value of b:", b)

2. Addition of Two Integers

# Input integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Add the integers
sum_result = num1 + num2

# Print the result
print("The sum of", num1, "and", num2, "is", sum_result)


3. Arithmetic Operations on Integers

# Input two integers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Perform arithmetic operations
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x // y)  # Integer division
print("Remainder:", x % y)  # Modulus operation


4. Swapping Two Integer Values

# Input integers
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Swap values
a, b = b, a

# Print swapped values
print("After swapping:")
print("a =", a)
print("b =", b)


5. Calculate the Area of a Rectangle (Using Integers)

# Input length and width
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Calculate area
area = length * width

# Print result
print("The area of the rectangle is:", area)


6. Check if an Integer is Positive, Negative, or Zero

# Input an integer
num = int(input("Enter an integer: "))

# Check the integer's sign
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print("The number is zero")

7. Multiply Integer by Itself (Square)

# Input an integer
num = int(input("Enter an integer: "))

# Calculate square
square = num * num

# Print result
print("The square of", num, "is", square)


8. Find the Larger of Two Integers

# Input integers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Find the larger number
if a > b:
    print(a, "is larger")
elif b > a:
    print(b, "is larger")
else:
    print("Both numbers are equal")


9. Check if an Integer is Divisible by Another

# Input two integers
num1 = int(input("Enter the numerator: "))
num2 = int(input("Enter the denominator: "))

# Check divisibility
if num1 % num2 == 0:
    print(num1, "is divisible by", num2)
else:
    print(num1, "is not divisible by", num2)


10. Generate a Range of Integer Values

# Input start and end values
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

# Generate range of integers
print("The range of integers from", start, "to", end, "is:")
for i in range(start, end + 1):
    print(i, end=" ")

1. Evaluate a Mathematical Expression

# Input a mathematical expression as a string
expression = input("Enter a mathematical expression (e.g., 5 + 2 * 3): ")

# Evaluate the expression
result = eval(expression)

# Print the result
print("The result of the expression is:", result)


2. Perform Operations on User-Defined Values

# Input numbers and operation as a string
expression = input("Enter an operation with two numbers (e.g., 10 + 20): ")

# Evaluate the operation
result = eval(expression)

# Print the result
print("The result is:", result)


3. Calculate Area of a Circle Using eval()

import math

# Input radius using eval
radius = eval(input("Enter the radius of the circle: "))

# Calculate area
area = math.pi * radius ** 2

# Print the area
print("The area of the circle is:", area)


4. Evaluate a User-Defined Formula

# Input a formula
formula = input("Enter a formula using x (e.g., x**2 + 2*x + 1): ")

# Input the value of x
x = eval(input("Enter the value of x: "))

# Evaluate the formula
result = eval(formula)

# Print the result
print("The result of the formula is:", result)


5. Evaluate Multiple Expressions

# Input multiple expressions separated by commas
expressions = input("Enter expressions separated by commas (e.g., 2+3, 5*4, 10/2): ")

# Split and evaluate each expression
results = [eval(expr.strip()) for expr in expressions.split(",")]

# Print the results
print("Results of the expressions are:", results)


6. Validate a Safe Use of eval()

# Input an expression
expression = input("Enter a mathematical expression (e.g., 3 + 5): ")

# Allow only safe characters (numbers, +, -, *, /, etc.)
if all(char in "0123456789+-*/(). " for char in expression):
    # Evaluate the expression
    result = eval(expression)
    print("The result is:", result)
else:
    print("Invalid input. Only numbers and operators are allowed.")


Program: Operator Precedence and Associativity

# Demonstrating Operator Precedence
print("Operator Precedence Examples:")

# Multiplication (*) has higher precedence than addition (+)
result1 = 5 + 3 * 2
print("5 + 3 * 2 =", result1)  # Output: 5 + (3 * 2) = 11

# Parentheses change the order of evaluation
result2 = (5 + 3) * 2
print("(5 + 3) * 2 =", result2)  # Output: (8) * 2 = 16

# Division (/) and Multiplication (*) have the same precedence, evaluated left-to-right
result3 = 10 / 2 * 3
print("10 / 2 * 3 =", result3)  # Output: (10 / 2) * 3 = 15.0

# Exponentiation (**) has higher precedence than multiplication (*)
result4 = 2 * 3 ** 2
print("2 * 3 ** 2 =", result4)  # Output: 2 * (3 ** 2) = 18

# Parentheses force a different evaluation order
result5 = (2 * 3) ** 2
print("(2 * 3) ** 2 =", result5)  # Output: (6) ** 2 = 36

# Demonstrating Associativity
print("\nOperator Associativity Examples:")

# Exponentiation (**) is right-to-left associative
result6 = 2 ** 3 ** 2
print("2 ** 3 ** 2 =", result6)  # Output: 2 ** (3 ** 2) = 2 ** 9 = 512

# Addition (+) and Subtraction (-) are left-to-right associative
result7 = 10 - 5 + 3
print("10 - 5 + 3 =", result7)  # Output: (10 - 5) + 3 = 8

# Division (/) and Multiplication (*) are left-to-right associative
result8 = 100 / 10 / 2
print("100 / 10 / 2 =", result8)  # Output: (100 / 10) / 2 = 5.0


Output Explanation:
Operator Precedence:
Operators like ** (exponentiation) have higher precedence than *, /, +, and -.
Parentheses () can override the default precedence.
Operator Associativity:
Most operators (like +, -, *, /) are left-to-right associative.
Exponentiation ** is right-to-left associative.

Sample Output:

Operator Precedence Examples:
5 + 3 * 2 = 11
(5 + 3) * 2 = 16
10 / 2 * 3 = 15.0
2 * 3 ** 2 = 18
(2 * 3) ** 2 = 36

Operator Associativity Examples:
2 ** 3 ** 2 = 512
10 - 5 + 3 = 8
100 / 10 / 2 = 5.0


1. Newline (\n) Example

# String with newline control code
print("Hello, Python!\nWelcome to control codes.")

Output:

Hello, Python!
Welcome to control codes.


2. Tab (\t) Example

# String with tab control code
print("Name\tAge\tCountry")
print("Alice\t25\tUSA")
print("Bob\t30\tUK")

Output:

Name    Age    Country
Alice   25     USA
Bob     30     UK


3. Backslash (\\) Example

# String with a backslash
print("This is a backslash: \\")

Output:

This is a backslash: \


4. Single Quote (\') and Double Quote (\") Example

# String with escaped quotes
print('She said, \'Hello!\'')  # Single quote
print("He replied, \"How are you?\"")  # Double quote

Output:

She said, 'Hello!'
He replied, "How are you?”


5. Carriage Return (\r) Example

# String with carriage return
print("Hello, World!\rPython")

Output:

Python

Explanation: The text after \r (Python) overwrites "Hello, World!".

6. Bell (\a) Example

# String with bell control code
print("Alert sound\a")

Output:
Produces a beep sound (if your system supports it).

7. Form Feed (\f) Example

# String with form feed
print("Page 1\fPage 2")

Output:

Page 1
Page 2

Explanation: \f may behave differently on some systems or printers.

8. Unicode Characters Example

# String with Unicode characters
print("Smiley Face: \u263A")
print("Heart Symbol: \u2764")

Output:

Smiley Face: ☺
Heart Symbol: ❤


9. Combining Multiple Control Codes

# Combining different control codes
print("Name\tAge\tCountry\nAlice\t25\tUSA\nBob\t30\tUK\nPath: C:\\Program Files\\Python")

Output:

Name    Age    Country
Alice   25     USA
Bob     30     UK
Path: C:\Program Files\Python

10. Raw String (Ignoring Control Codes)

# Using raw strings to ignore control codes
print(r"Path with raw string: C:\Program Files\Python")

Output: Path with raw string: C:\Program Files\Python

—---------------------------------------------------------------------------------------------------

1.write a programme in python to shows all operator precedence
def evaluate_expression():
    print("Welcome to the Expression Evaluator!")
    print("You can enter any valid Python expression (e.g., 2 + 3 * (4 - 1)).")
    print("Type 'exit' to quit the program.\n")

    while True:
        user_input = input("Enter an expression: ")

        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        try:
            # Evaluate the expression using eval()
            result = eval(user_input)
            print(f"Result: {result}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    evaluate_expression()

************************************************************************************************************************
************************************************************************************************************************
************************************************************************************************************************
Unit_2 Practical Assignment

1. Boolean Expressions
Boolean expressions evaluate to True or False. They are commonly used in conditional statements.
Example:
x = 10
y = 20

print(x > y)   # False
print(x < y)   # True
print(x == y)  # False
print(x != y)  # True


2. The Simple if Statement
An if statement executes a block of code only if its condition evaluates to True.
Example:
python
Copy code
age = 18

if age >= 18:
    print("You are eligible to vote.")

Output:
You are eligible to vote.


3. The if/else Statement
The if/else statement provides an alternative block of code when the condition is False.
Example:


age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

Output:

You are not eligible to vote.


4. Compound Boolean Expressions
Compound boolean expressions combine multiple conditions using logical operators (and, or, not).
Example:

age = 25
income = 50000

if age > 18 and income > 40000:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")

Output:

You are eligible for the loan.


5. Nested Conditionals
Nested conditionals allow placing one if statement inside another.
Example:

age = 20
citizenship = "US"

if age >= 18:
    if citizenship == "US":
        print("You are eligible to vote in the US.")
    else:
        print("You are not a US citizen.")
else:
    print("You are too young to vote.")

Output:
css
Copy code
You are eligible to vote in the US.


6. Multi-way Decision Statements
Multi-way decision-making is achieved using if, elif, and else.
Example:

grade = 85

if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C.")
else:
    print("You need to work harder.")

Output:
css
Copy code
You got a B!


1. Conditional Expressions (Ternary Operator)
Conditional expressions (also called ternary operators) allow you to write a simple if-else in a single line.
Syntax:
python
Copy code
value_if_true if condition else value_if_false

Example:

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult


2. Errors in Conditional Statements
Errors can occur in conditional statements due to syntax issues, logical mistakes, or incorrect indentation. Here are some common examples:
Syntax Error:
python
Copy code
if x > 10     # Missing colon (:) causes a syntax error
    print("x is greater than 10")

Logical Error:
python
Copy code
x = 5
if x < 10:
    print("x is greater than 10")  # Incorrect logic (should check `x > 10`)

Indentation Error:
python
Copy code
x = 10
if x > 5:
print("x is greater than 5")  # Improper indentation causes an error


3. Iteration: The while Statement
A while loop is used for indefinite iteration, where the loop continues as long as the condition is True.
Example:
python
Copy code
count = 1
while count <= 5:
    print(count)
    count += 1

Output:
Copy code
1
2
3
4
5


4. Definite Loops vs. Indefinite Loops
Definite Loops
Definite loops are used when the number of iterations is known beforehand, typically using a for loop.
Example (Definite Loop):
python
Copy code
for i in range(5):  # Loop will iterate exactly 5 times
    print(i)

Output:
Copy code
0
1
2
3
4


Indefinite Loops
Indefinite loops are used when the number of iterations is unknown and depends on a condition, typically using a while loop.
Example (Indefinite Loop):
python
Copy code
user_input = ""
while user_input != "stop":
    user_input = input("Enter a command (type 'stop' to quit): ")
    print(f"You entered: {user_input}")


Key Differences Between Definite and Indefinite Loops
Feature
Definite Loops
Indefinite Loops
Type of Loop
for loop
while loop
Iterations Known
Known beforehand
Unknown; depends on a condition
Use Case
Iterating over a range, list, etc.
Waiting for a specific condition


Practical Examples
Combining Conditional Expressions with Loops

numbers = [1, 2, 3, 4, 5]
even_or_odd = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(even_or_odd)

Output:

['Odd', 'Even', 'Odd', 'Even', 'Odd']

Using while for Input Validation

user_age = -1
while user_age < 0:
    try:
        user_age = int(input("Enter a valid age (>= 0): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
print(f"You entered a valid age: {user_age}")

1. The for Statement
The for loop iterates over a sequence (like a list, string, or range).
Example:

# Iterate through a range of numbers
for i in range(1, 6):
    print(i)

Output:
Copy code
1
2
3
4
5


2. Nested Loops
A nested loop is a loop inside another loop.
Example:

# Print a multiplication table
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"{i} * {j} = {i * j}")

Output:
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9


3. Abnormal Loop Termination
Loops can terminate prematurely using break or skip iterations using continue.
Example with break:
python
Copy code
for i in range(1, 10):
    if i == 5:
        break
    print(i)

Output:

1
2
3
4

Example with continue:
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

Output:

1
2
4
5


4. Infinite Loops
An infinite loop runs indefinitely unless interrupted.
Example:

# A simple infinite loop
while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == "exit":
        break


5. Computing Square Root
Using the math module:

import math

num = 16
sqrt = math.sqrt(num)
print(f"The square root of {num} is {sqrt}")

Custom method (Newton's Method):

def newton_sqrt(number):
    guess = number / 2.0
    for _ in range(20):  # Iterate to improve accuracy
        guess = (guess + number / guess) / 2.0
    return guess

print(newton_sqrt(16))  # Output: 4.0


6. Drawing a Tree
Using ASCII:

def draw_tree(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
    print(" " * (height - 1) + "|")

draw_tree(5)

Output:
markdown

   *
   ***
  *****
 *******
*********
    |

Using Turtle:

import turtle

def draw_tree(branch_length):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(20)
        draw_tree(branch_length - 15)
        turtle.left(40)
        draw_tree(branch_length - 15)
        turtle.right(20)
        turtle.backward(branch_length)

turtle.left(90)
draw_tree(100)
turtle.done()


7. Printing Prime Numbers
Example:

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Print primes from 1 to 50
for num in range(1, 51):
    if is_prime(num):
        print(num, end=" ")

Output:

2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

8.Using Raise to Trigger Exception
python

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    print(divide(10, 0))
except ValueError as e:
    print(e)

************************************************************************************************************************
************************************************************************************************************************
************************************************************************************************************************




## Functions

### 1. Introduction to Using Functions
```python
# Function to calculate the square of a number
def square(number):
    return number * number

print(square(4))
```

### 2. Standard Mathematical Functions
```python
# Using math library
import math
number = 16
print(f"Square root of {number}: {math.sqrt(number)}")
```

### 3. Time Functions
import time 
start_time = time.time()  # Records the start time
for i in range(1000000):   # Loops through 1,000,000 iterations
    pass                            # Empty loop (does nothing)
end_time = time.time()    # Records the end time
# Prints the execution time by subtracting the start time from the end time
print(f"Execution time: {end_time - start_time} seconds")



### 4. Random Numbers
```python
# Generate random numbers
import random
print(random.randint(1, 100))
```

### 5. Function Basics
```python
# Function to add two numbers
def add(a, b):
    return a + b

print(add(3, 5))
```

### 6. Using Functions Main Function
```python
# Main function example
def main():
    print("This is the main function")

if __name__ == "__main__":
    main()
```

### 7. Parameter Passing
```python
# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

### 8. Function Examples

#### Better Organized Prime Generator
```python
# Prime number generator
def is_prime(num):
    if num < 2:
        return False
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False
    return True

def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

print(generate_primes(10, 50))
```

#### Command Interpreter
```python
# Simple command interpreter
def interpreter(command):
    if command == "start":
        print("System starting...")
    elif command == "stop":
        print("System stopping...")
    else:
        print("Unknown command")

interpreter("start")
```

#### Restricted Input
```python
# Input validation
def get_positive_number():
    while True:
        try:
            num = int(input("Enter a positive number: "))
            if num > 0:
                return num
            else:
                print("Number must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

print(get_positive_number())
```

### 9. Recursion

#### Making Functions Reusable
```python
# Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

#### Documenting Functions and Modules
```python
# Example with docstrings
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add(3, 4))
print(add.__doc__)
```

#### Functions as Data

# Passing functions as arguments
def apply_function(func, value):
    return func(value)


def square(n):
    return n * n

print(apply_function(square, 5))



## Lists

### 1. Using Lists

# Basic list operations
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)


### 2. List Assignment and Equivalence
# Demonstrating shallow copy
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # Both lists change
```

### 3. List Bounds
# Handling index errors
numbers = [10, 20, 30]
try:
    print(numbers[5])
except IndexError:
    print("Index out of bounds")
```

### 4. Slicing
# List slicing
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])
```

### 5. Lists and Functions

# Passing lists to functions
def square_elements(lst):
    return [x * x for x in lst]

print(square_elements([1, 2, 3, 4]))


### 6. Prime Generation with a List

# Store primes in a list
def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                break
        else:
            primes.append(num)
    return primes

print(generate_primes(50))


### 7. List Processing
# Filtering even numbers
def filter_evens(numbers):
    return [num


###7  Sorting a List (Bubble Sort)
1 # Bubble sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print("Sorted List:", bubble_sort([5, 2, 9, 1, 5]))


—-------------------------------------------------------------------------------------------------------------------
EXTRA PRACTICE QUESTION

Create a user defined function to print count for given range.
Write a function that takes an integer n and returns a random integer with exactly n digits.
#Maximum range is 5
#For instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not #because that is really 93, which is a two-digit number.
Write a function that converts temperatures from Celsius to Fahrenheit
Create a user defined function to find the sum of digits of a number.
Create a user defined function to find the sum of digits of a number.If the sum is more than 9 then call the same function again and again till the sum is between 0 to 9. (i.e Find super digit, use recursion)
By using a recursive function find the factorial of a given number.
Write a function called rectangle that takes two integers m and n as arguments and prints out an m× n box consisting of asterisks. Shown below is the output of rectangle(2,4)
****
****
Write a function that takes an integer n and returns a random integer with exactly n digits. For instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because that is really 93, which is a two-digit number.
Write a function called root that is given a number x and an integer n and returns x power 1/n. In the function deﬁnition, set the default value of n to 2.
create a user defined function which takes two user defined parameters, add them and return the sum of it.
Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.
Write a program that generates a list L of 50 random numbers between 1 and 100.
Write a program to perform following tasks:
- Read a list of integers from a user.
- Remove duplicate values from this list. We call it a super list.
- In a single scan of the super list, perform following operations:
- If the number is not perfectly divisible by 3, discard it.
- If the number is greater than 30, add 5 to it. Else, subtract 5 from it.
- Display contents of the list.
Create a list with different types of elements. Iterate over the list and print every element and type of element
Write a program that generates a list of 20 random numbers between 1 and 100.
 Print the list.
 Print the average of the elements in the list.
 Print the largest and smallest values in the list.
 Print the second largest and second smallest entries in the list
 Print how many even numbers are in the list.
Perform following functionalities:
Generate a list containing 100 similar words.
Replace each element in a list L with its square.
Count how many items in a list L are greater than 50.
Write a program that generates a list of 20 random numbers between 1 and 100.
Print the list.
Print the average of the elements in the list.
Print the largest and smallest values in the list.
Print the second largest and second smallest entries in the list
Print how many even numbers are in the list.

1. User-defined function to print count for given range
python
Copy
Edit
def print_count(start, end):
    for i in range(start, end + 1):
        print(i)
                                                                                                                                                                                                                
2. Return a random integer with exactly n digits (max range 5)
python
Copy
Edit
import random

def random_n_digit(n):
    if 1 <= n <= 5:
        return random.randint(10**(n-1), 10**n - 1)
    else:
        raise ValueError("Only up to 5 digits allowed")
                                                                                                                                                                                                                
3. Convert Celsius to Fahrenheit
python
Copy
Edit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
                                                                                                                                                                                                                
4. Sum of digits of a number
python
Copy
Edit
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
                                                                                                                                                                                                                
5. Find super digit using recursion
python
Copy
Edit
def super_digit(n):
    if n < 10:
        return n
    return super_digit(sum_of_digits(n))
  
6. Recursive factorial function
python
Copy
Edit
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
  
7. Print rectangle of m × n asterisks
python
Copy
Edit
def rectangle(m, n):
    for _ in range(m):
        print('*' * n)
  
8. Random integer with exactly n digits (repeated)
python
Copy
Edit
# Already covered in section 2
  
9. Root function with default value n=2
python
Copy
Edit
def root(x, n=2):
    return x ** (1 / n)
  
10. Add two user-defined parameters and return the sum
python
Copy
Edit
def add_numbers(a, b):
    return a + b
  
11. Generate list of 20 random numbers and perform tasks
python
Copy
Edit
import random

def list_analysis():
    L = [random.randint(1, 100) for _ in range(20)]
    print("List:", L)
    print("Average:", sum(L) / len(L))
    print("Largest:", max(L))
    print("Smallest:", min(L))
    print("Second Largest:", sorted(set(L))[-2])
    print("Second Smallest:", sorted(set(L))[1])
    print("Even count:", sum(1 for x in L if x % 2 == 0))
  
12. Generate list of 50 random numbers
python
Copy
Edit
def random_50():
    return [random.randint(1, 100) for _ in range(50)]
  
13. Read user list, remove duplicates, and process
python
Copy
Edit
def process_user_list():
    user_input = input("Enter integers separated by space: ")
    numbers = list(map(int, user_input.split()))
    super_list = list(set(numbers))

    result = []
    for num in super_list:
        if num % 3 != 0:
            continue
        result.append(num + 5 if num > 30 else num - 5)

    print("Processed List:", result)
              
14. Iterate list with different element types and print
python
Copy
Edit
def print_list_types():
    mixed_list = [42, "hello", 3.14, True, None, [1,2], {"a":1}]
    for item in mixed_list:
        print(f"Element: {item}, Type: {type(item)}")
              
15. Generate 100 similar words (e.g., 'hello')
python
Copy
Edit
def similar_words():
    return ["hello"] * 100
              
16. Replace each element in list with its square
python
Copy
Edit
def square_elements(L):
    return [x**2 for x in L]
              
17. Count how many items in list are greater than 50
python
Copy
Edit
def count_above_50(L):
    return sum(1 for x in L if x > 50)
              
18. Print list of 20 numbers and statistics (repeated)
python
Copy
Edit
# Already covered in section 11


************************************************************************************************************************
************************************************************************************************************************
************************************************************************************************************************

Unit_4 Practical Assignment 

# Python: Objects Using Objects

Objects are instances of classes and are fundamental in Python's object-oriented programming paradigm.

### Example: Creating and Using an Object
# Define a simple class

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

# Create an object
my_dog = Dog("Buddy", 3)

# Access attributes and methods
print(my_dog.name)  # Output: Buddy
print(my_dog.bark())  # Output: Buddy says Woof!


## String Objects

Python strings are immutable objects. They come with numerous built-in methods for manipulation.

### Example: String Methods

# Create a string object
s = "Hello, World!"

# Accessing string methods
print(s.lower())  # Output: hello, world!
print(s.upper())  # Output: HELLO, WORLD!
print(s.replace("World", "Python"))  # Output: Hello, Python!
print(s.split(", "))  # Output: ['Hello', 'World!']

# String slicing
print(s[0:5])  # Output: Hello


## List Objects

Lists are mutable objects in Python and can hold items of different data types. They also have several methods for data manipulation.

### Example: List Methods

# Create a list object
fruits = ["apple", "banana", "cherry"]

# Accessing list methods
fruits.append("date")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'date']

fruits.sort()
print(fruits)  # Output: ['apple', 'cherry', 'date']

# Accessing elements
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: date

# Slicing a list
print(fruits[1:])  # Output: ['cherry', 'date']


### Example: Nested Lists

# Create a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a nested list
print(matrix[0])  # Output: [1, 2, 3]
print(matrix[1][1])  # Output: 5

# Iterating through a nested list
for row in matrix:
    print(row)

Create a BankAccount class with deposit and withdraw methods. Implement balance checking before withdrawal.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")

acc = BankAccount("John Doe", 500)
acc.deposit(200)
acc.withdraw(100)
acc.withdraw(700)  # Should show "Insufficient funds!"

Create an Abstract Class Shape with an abstract method area(), then implement Circle and Rectangle.
from abc import ABC, abstractmethod
class Shape(ABC):
    #@abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

c = Circle(7)
r = Rectangle(5, 10)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())



Implement a Stack ADT using a Python class with push(), pop(), and peek() methods.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(10)
s.push(20)
print("Top:", s.peek())
print("Popped:", s.pop())
print("Popped:", s.pop())
print("Popped:", s.pop())  # Should display "Stack is empty"

Tuple
Create a tuple, access elements, and perform slicing operations.

my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slice [1:4]:", my_tuple[1:4])

Write a program to find the maximum and minimum values in a tuple.

numbers = (5, 2, 8, 1, 9, 7)
print("Max:", max(numbers))
print("Min:", min(numbers))

Convert a tuple to a list and modify its elements.

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.append(6)
print("Modified List:", my_list)

—------------------------------------------------------------------------------------------------
# a) Create a tuple of integers
numbers = (10, 20, 30, 40, 50, 60, 70)

# b) Access and display specific elements using indexing
print("Element at index 0:", numbers[0])
print("Element at index 3:", numbers[3])
print("Element at last index (-1):", numbers[-1])

# c) Perform and display various slicing operations
print("First three elements:", numbers[:3])
print("Last three elements:", numbers[-3:])




Set
Create a set, add elements, and remove an element.

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(2)
print("Set after modifications:", my_set)
Find the union, intersection, and difference of two sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
Check if an element is present in a set.

my_set = {10, 20, 30, 40, 50}
print(30 in my_set)  # True
print(100 in my_set) # False

Dictionary
##Create a dictionary and print keys and values.
student = {"name": "Alice", "age": 21, "marks": 85}
print("Keys:", student.keys())
print("Values:", student.values())
print("Name:", student["name"])

Write a program to update an existing dictionary.

student = {"name": "Alice", "age": 21, "marks": 85}
student["marks"] = 90  # Updating value
student["city"] = "New York"  # Adding new key-value pair
print("Updated Dictionary:", student)

##Find the frequency of words in a given string using a dictionary.

text = "apple banana apple orange banana apple"
words = text.split()
freq_dict = {}

for word in words:
    freq_dict[word] = freq_dict.get(word, 0) + 1

print("Word Frequency:", freq_dict)


Simple Algorithms
Find the factorial of a number using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 5
print("Factorial of", num, "is", factorial(num))

Find whether a number is prime or not.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = 29
print(num, "is Prime:", is_prime(num))

Fibonacci series using recursion.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

num = 6
for i in range(num):
    print(fibonacci(i), end=" ")

Data Structures
Stack (Using List)
##Implement a stack with push and pop operations.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(10)
s.push(20)
print("Popped:", s.pop())
print("Popped:", s.pop())
print("Popped:", s.pop())  # Should display "Stack is empty"
Queue (Using List)
Implement a queue using a list with enqueue and dequeue operations.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())  # Should display "Queue is empty"
Linear Search
Write a program to implement Linear Search.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [10, 20, 30, 40, 50]
target = 30
result = linear_search(numbers, target)
print(f"Element {target} found at index {result}" if result != -1 else "Element not found")
Binary Search
Write a program to implement Binary Search.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers = [10, 20, 30, 40, 50]
target = 30
result = binary_search(numbers, target)
print(f"Element {target} found at index {result}" if result != -1 else "Element not found")


Exception Examples
Handling Division by Zero Exception


 try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

Handling Multiple Exceptions (ValueError & ZeroDivisionError)

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter integers only.")

Handling FileNotFoundError


try:
    file = open("non_existent_file.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File not found!")


Using Exceptions
Handling Exception with finally Block

try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("Execution Completed.")

Using else with Exception Handling

try:
    num = int(input("Enter a number: "))
    print(f"Square of {num} is {num ** 2}")
except ValueError:
    print("Error: Invalid input, enter a number.")
else:
    print("No exception occurred, successful execution.")

Catching All Exceptions (Generic Exception Handling)

try:
    value = int(input("Enter a number: "))
    print(10 / value)
except Exception as e:
    print("An error occurred:", e)

Custom Exceptions
Practical Programs (10-15 Marks Each)
##Creating a Custom Exception for Negative Numbers


class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Error: Negative number entered!")
    print("You entered:", num)
except NegativeNumberError as e:
    print(e)

##Custom Exception for Age Validation

class InvalidAgeError(Exception):
    def __init__(self, message="Age must be between 18 and 100"):
        self.message = message
        super().__init__(self.message)

try:
    age = int(input("Enter your age: "))
    if age < 18 or age > 100:
        raise InvalidAgeError()
    print("Valid age entered:", age)
except InvalidAgeError as e:
    print(e)
Bank Withdrawal Custom Exception

--------------------------------------------------------------------------------------------------------        

# Custom Exception
class InsufficientFundsError(Exception):
    def __init__(self, message="Withdrawal amount exceeds available balance."):
        self.message = message
        super().__init__(self.message)

# Bank Account Class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            raise InsufficientFundsError(f"Attempted to withdraw {amount}, but only {self.__balance} is available.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def display_account_info(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Current Balance: {self.__balance}")

# Main Program
def main():
    account = BankAccount("John Doe", 1000)
    account.display_account_info()

    account.deposit(500)

    try:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    except InsufficientFundsError as e:
        print("Withdrawal failed:", e)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

    print("Final Balance:", account.get_balance())

if __name__ == "__main__":
    main()

—--------------------------------------------------------------
Write a Python program to perform the following operations on a tuple:
a) Create a tuple of 10 integers.
 b) Access and display the 1st, 5th, and last elements using indexing.
 c) Perform and display the results of the following slicing operations:

def main():
    # a) Creating a tuple of integers
    numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    print("Original Tuple:", numbers)

    # b) Accessing specific elements using indexing
    print("1st Element:", numbers[0])
    print("5th Element:", numbers[4])
    print("Last Element:", numbers[-1])

    # c) Performing slicing operations
    print("First 5 Elements:", numbers[:5])
    print("Last 3 Elements:", numbers[-3:])
    print("Every 2nd Element:", numbers[::2])
    print("Reversed Tuple:", numbers[::-1])

main()

