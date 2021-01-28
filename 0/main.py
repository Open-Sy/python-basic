import csv
from collections import Counter

with open('data.csv','r', newline='\n') as f:
    raw_data = csv.reader(f)
    data = [i for i in raw_data]

print(data)

results = []

for sample in data:
    print(sample)
    sample = [int(i) for i in sample]

    mean = sum(sample) / len(sample)
    print('mean :', mean)

    n = len(sample)
    index = n // 2
    if n % 2:
        median = sorted(sample)[index]
    median = sum(sorted(sample)[index - 1:index + 1]) / 2
    print('median :', median)

    c = Counter(sample)
    mode = [k for k, v in c.items() if v == c.most_common(1)[0][1]]
    print('mode :', mode, type(mode))

    results.append([mean,median,mode])

with open('calculated_results.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(results)


