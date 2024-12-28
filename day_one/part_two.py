first = []
second = dict()


with open('data.txt') as data:
    for line in data:
        clean = line.replace('\n', '');
        numbers = clean.split('   ')
        first.append(int(numbers[0]))
        if int(numbers[1]) in second:
            second[int(numbers[1])] += 1
        else:
            second[int(numbers[1])] = 1

similarity = 0
for item in first:
    if item in second:
        similarity += item * second[item]

print(similarity)
