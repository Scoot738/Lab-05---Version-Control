def add_numbers(a, b):
	return a + b
    
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)
	
result = add_numbers(3, 5)
print(result)

numbers = [2, 4, 6, 8, 10]
average = calculate_average(numbers)
print(average)