
first = []
second = []


with open('data.txt') as data:
    for line in data:
        numbers = line.split('   ')
        first.append(int(numbers[0]))
        second.append(int(numbers[1]))


first.sort()
second.sort()

distance = 0
for (index, item) in enumerate(first):
    distance += abs(second[index] - item)

print(distance)
