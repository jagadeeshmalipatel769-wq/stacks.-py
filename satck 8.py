def factorial(n):
    print(f"Entering factorial({n})")

    if n == 0:
        print("Base case reached, returning 1")
        return 1

    result = n * factorial(n - 1)
    print(f"Returning from factorial({n}), result: {result}")
    return result


answer = factorial(4)
print("Final answer:", answer)