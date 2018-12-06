from collections import defaultdict

sum = 0
count = defaultdict(int)
result = None

with open('input.txt', 'r') as f:
    for a in f:
        sum += int(a)
        count[sum] += 1
        if count[sum] > 1:
            result = sum
            break


while result == None: 
    final_value = sum
    tmp_count = list(count.keys())
    for key in tmp_count:
        sum = key + final_value
        count[sum] += 1
        if count[sum] > 1:
            result = sum
            break

print(result)

