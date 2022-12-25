numbers = [99, 8, 396, 8, 99, 396]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)