
search_words = ['Python', 'C', 'OOP', 'Hello', 'Java']
file = open('input.txt', 'r')
counts = dict()

for word in search_words:
    counts[word.lower()] = 0


for line in file:
    # print(line.strip())
    for item in search_words:
        if line.strip().lower() == item.lower():
            counts[item.lower()] += 1

file.close()

# print(counts)

for k,v in counts.items():
    for word in search_words:
        if word.lower() == k:
            print(f'{word} -> {v}')