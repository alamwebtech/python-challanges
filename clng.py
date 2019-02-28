a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(a)

choice = int(input("Pick a number from the list: "))
print("\n")
result = []

for i in a:
	if choice not in a:
		print(f"{choice}, this number does not exist in the given list.\n")
		break
	elif choice < i:
		result.append(i)
	else:
		print(f"{result}This is the list and it contains all the numbers that smaller than what you chossed.\n")
		break
	print("End of the program")