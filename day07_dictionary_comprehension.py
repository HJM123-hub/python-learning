numbers = range(1, 6)

squares = {number: number * number for number in numbers}

print(f"Square dictionary: {squares}")
even_squares = {number: number * number for number in numbers if number % 2 == 0}

print(f"Even square dictionary: {even_squares}")