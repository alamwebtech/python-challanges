#Challenge No 1

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



#Challenge No 2

num = int(input("Please choose a number:" ))

range_num = list(range(1,num +1))

list_num = []

for i in range_num:
	if num % i == 0:
	list_num.append(i)

print(list_num)


#Challenge No 3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_num = []


for i in a:
	if i in b and i not in common_num:
		what.append(i)
print(common_num)

