sum = 0
with open('input.txt', 'r') as f:
	for num in f:
		sum += int(num)

print(sum)
