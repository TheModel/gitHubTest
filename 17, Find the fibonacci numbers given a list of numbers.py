# This program takes in a list of numbers as input and print all the fibonacci numbers.


def fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    return fib_list

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
print("Fibonacci numbers:")
for num in input_list:
    fib_nums = fibonacci(num)
    print(f"Fibonacci numbers for {num}: {fib_nums}")


