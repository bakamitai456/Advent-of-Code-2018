min_diff = None
diff_word = None
store_words = []

with open('input.txt', 'r') as f:
    for word in f:
        if len(word) > 0:
            for store_word in store_words:
                diff = 0
                cutting_word = ''
                for i in range(len(store_word if len(store_word) < len(word) else word)):
                    x = word[i]
                    y = store_word[i]
                    if x != y:
                        diff += 1
                    else:
                        cutting_word += x

                    if min_diff != None and diff > min_diff:
                        break
                
                diff += abs(len(store_word) - len(word))
                if min_diff == None or diff < min_diff:
                    min_diff = diff
                    diff_word = cutting_word

            store_words.append(word)

print(diff_word)
print(min_diff)
