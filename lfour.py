# Recursive
print('This program calculates factorial.')
def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n - 1)



user_input = input('Enter a number:')
print('Result:', factorial(user_input))


