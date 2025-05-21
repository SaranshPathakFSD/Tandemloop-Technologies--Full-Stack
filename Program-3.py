def generate_conditional_series(a: int):
    result = []
    for i in range(1, a + 1, 2):
        result.append(i)
    return result

# Example
a = int(input("Enter a: "))
print(generate_conditional_series(a))
