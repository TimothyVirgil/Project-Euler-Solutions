# Solution to Project Euler Problem 1
# Code by Tim Payne
# Completed: 03/14/2019

solution = 0

for a in range(1000):

	if a % 3 == 0 or a % 5 == 0:

		solution += a

print(solution)







