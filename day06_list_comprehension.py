numbers = range(1, 11)

squares = [number * number for number in numbers]
print(f"Squares: {squares}")

even_numbers = [number for number in numbers if number % 2 == 0]

print(f"Even numbers: {even_numbers}")
odd_numbers = [number for number in numbers if number % 2 != 0]

print(f"Odd numbers: {odd_numbers}")