sample = [23, 27, 44, 1, 14, 17, 100, 49, 99]
# sample.sort(reverse = True)
# print(sample)

sort_sample = []

while sample:
    minimum = sample[0]
    for i in sample:
        if i > minimum:
            minimum = i
    sort_sample.append(i)
    sample.pop(i)

print(sort_sample)


