from collections import defaultdict

double = 0
triple = 0

with open('input.txt', 'r') as f:
    for word in f:
        char_count = defaultdict(int)
        is_triple = False
        is_double = False
        for char in word:
            char_count[char] += 1
        
        for char in char_count.keys():
            if char_count[char] == 3:
                is_triple = True
            elif char_count[char] == 2:
                is_double = True

        if is_double:
            double += 1
        if is_triple:
            triple += 1

result = double * triple
print(double)
print(triple)
print(result)