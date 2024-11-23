def greet_user(name):
    """Greets the user with their name."""
    return f"Hello,{name}!Welcome to Python programming."
print(greet_user("Usman"))

def add_numbers(num1, num2):
    """Adds two numbers and returns the result."""
    return num1 + num2
print(add_numbers(5,10))

def check_even_odd(number):
    """Checks of a number is even or odd."""
    return"Even" if number % 2 ==0 else "odd"
print(check_even_odd(7))
print(check_even_odd(8))

def find_largest(num1,num2,num3):
    """Finds and returns the largest of three numbers."""
    return max(num1,num2,num3)
print(find_largest(10,20,15))

def calculate_factorial(n):
    """Calculates the factorial of a number."""
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial
print(calculate_factorial(5))

def reverse_string(text):
    """Reverses the input string."""
    return text[::-1]
print(reverse_string("Python"))

def is_prime(number):
    """Checks if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))

def count_vowels(text):
    """Counts the number of vowels in the input string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print(count_vowels("I love Python programming."))

def find_max_in_list(numbers):
    """Finds the maximum number in a list."""
    return max(numbers)
print(find_max_in_list([3, 5, 2, 9, 1]))

def convert_temperature(temperature, scale):
    """Converts temperature between Celsius and Fahrenheit."""
    if scale == "C":
        return (temperature * 9/5) + 32  # 
    elif scale == "F":
        return (temperature - 32) * 5/9 
    else:
        return "Invalid scale"
def convert_temperature(temperature, scale):
    """Converts temperature between Celsius and Fahrenheit."""
    if scale == "C":
        return (temperature * 9/5) + 32  
    elif scale == "F":
        return (temperature - 32) * 5/9  
    else:
        return "Invalid scale"
print(convert_temperature(0, "C"))  
print(convert_temperature(32, "F"))

    