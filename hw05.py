from re import findall

# Task 1
def caching_fibonacci():
    """
    Creates and uses a cache to store and reuse already 
    calculated values ​​of Fibonacci numbers.
    """
    cache = dict()

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))

# Task 2
def generator_numbers(text):
    numbers = findall(r"\d+.\d+", text) # Looking for numbers
    if numbers:
        for number in numbers: # Return generator
            yield float(number)
    else:
        print("Дійсних чисел не знайдено")

def sum_profit(text, func):
    """
    Сalculates the total sum of numbers
    """
    total_income = 0
    for number in func(text):
        total_income += number
    return total_income

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")