def generate_series(n: int):
    result = []
    for i in range(n):
        result.append(2 * i + 1)
    return result

# Example
a = int(input("Enter a: "))
print(generate_series(a))
