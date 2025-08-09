
import os
import sys
import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def complex_function(x, y):
    result = (x**2 + y**2) / (x + y + 1)
    return result

def another_function(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

class MyClass:
    def __init__(self, name):
        self.name = name
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def remove_data(self, item):
        try:
            self.data.remove(item)
        except ValueError:
            print(f"{item} not found")

    def get_data(self):
        return self.data

def main():
    print("Starting script...")
    num = 10
    print(f"Factorial of {num}: {factorial(num)}")
    print(f"Fibonacci of {num}: {fibonacci(num)}")

    primes_to_check = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for p in primes_to_check:
        print(f"{p} is prime: {is_prime(p)}")

    x_val = 5
    y_val = 10
    print(f"Complex function result for ({x_val}, {y_val}): {complex_function(x_val, y_val)}")

    a_val = 100
    b_val = 200
    c_val = 150
    print(f"Maximum of ({a_val}, {b_val}, {c_val}): {another_function(a_val, b_val, c_val)}")

    my_object = MyClass("TestObject")
    my_object.add_data(1)
    my_object.add_data(2)
    my_object.add_data(3)
    print(f"My object data: {my_object.get_data()}")
    my_object.remove_data(2)
    print(f"My object data after removing 2: {my_object.get_data()}")
    my_object.remove_data(10) # This will print a message

    print("Script finished.")

if __name__ == "__main__":
    main()
