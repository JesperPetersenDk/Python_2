def j(n):
    return n * n

numbers = (5, 10, 20, 70)
result = map(j,numbers)
print(result)

numbersValue = set(result)
print(numbersValue)