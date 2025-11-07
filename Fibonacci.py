# Recursive Fibonacci with Step Count
def fibonacci_recursive(n, steps):
    steps[0] += 1  # Counting each function call as a step
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1, steps) + fibonacci_recursive(n - 2, steps)




# Iterative Fibonacci with Step Count
def fibonacci_iterative(n):
    steps = 0
    if n <= 1:
        return n, steps + 1  # Counting initial check as a step


    a, b = 0, 1
    for _ in range(2, n + 1):
        steps += 1  # Each iteration is a step
        a, b = b, a + b
    return b, steps




# Main program
def main():
    n = int(input("Enter the value of n to find the nth Fibonacci number: "))


    # Recursive method
    steps_recursive = [0]  # Using list for pass-by-reference
    fib_recursive = fibonacci_recursive(n, steps_recursive)
    print(f"Recursive: Fibonacci({n}) = {fib_recursive}, Steps = {steps_recursive[0]}")


    # Iterative method
    fib_iterative, steps_iterative = fibonacci_iterative(n)
    print(f"Iterative: Fibonacci({n}) = {fib_iterative}, Steps = {steps_iterative}")




if __name__ == "__main__":
    main()



#For Series:

def fib_non_recursive(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_series_recursive(n):
    return [fib_recursive(i) for i in range(n)]


n = int(input("Enter total numbers to print in Fibonacci series:\t"))


print("Fibonacci Series (non-recursive):", fib_non_recursive(n))
print("Fibonacci Series (recursive):    ", fib_series_recursive(n))





