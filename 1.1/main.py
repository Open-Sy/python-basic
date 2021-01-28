import csv
from collections import Counter

def calculate_mean(sample):
    mean = sum(sample) / len(sample)
    return mean

def calculate_median(sample):
    n = len(sample)
    index = n // 2
    if n % 2:
        median = sorted(sample)[index]
    median = sum(sorted(sample)[index - 1:index + 1]) / 2
    return median

def calculate_mode(sample):
    c = Counter(sample)
    mode = [k for k, v in c.items() if v == c.most_common(1)[0][1]]
    return mode

def write_results_to_file(output_file, results):
    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(results)


with open('data.csv','r', newline='\n') as f:
    raw_data = csv.reader(f)
    data = [i for i in raw_data]

print(data)

results = []
output_file = 'calculated_results.csv'

for sample in data:
    print(sample)
    sample = [int(i) for i in sample]

    mean = calculate_mean(sample)
    print('mean :', mean)

    median = calculate_median(sample)
    print('median :', median)

    mode = calculate_mode(sample)
    print('mode :', mode)

    results.append([mean,median,mode])

write_results_to_file( output_file, results)


