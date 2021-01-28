import csv
from collections import Counter

def calculate_mean(sample):
    '''
    sum of all data divided by the number of data
    '''
    mean = sum(sample) / len(sample)
    return mean

def calculate_median(sample):
    '''
    get the median value in the given data
    if the number of data is odd, it's okay to take the middle or median value
    if the number of data is even, there gonna be two median or middle value and we take smaller value as median
    '''
    n = len(sample)
    index = n // 2      # take floor division
    if n % 2:
        median = sorted(sample)[index]
    median = sum(sorted(sample)[index - 1:index + 1]) / 2
    return median

def calculate_mode(sample):
    '''
    get the most common values in the given sample data
    '''
    c = Counter(sample)
    mode = [k for k, v in c.items() if v == c.most_common(1)[0][1]]
    return mode

def write_results_to_file(output_file = 'output.csv', results = results):
    '''
    write calculate results to the file
    '''
    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(results)


results = []

# read the input file
with open('data.csv','r', newline='\n') as f:
    raw_data = csv.reader(f)
    data = [i for i in raw_data]

print(data)

# loop the data row by row and calculate mean, median, mode values
for sample in data:
    print(sample)

    # the data read from the csv comes with string type. To make calculation, we need to change these to integer type.
    sample = [int(i) for i in sample]

    # calculate mean
    mean = calculate_mean(sample)
    print('mean :', mean)

    # calculate median
    median = calculate_median(sample)
    print('median :', median)

    # calculate mode
    mode = calculate_mode(sample)
    print('mode :', mode)

    # append the calculated values to the results array
    results.append([mean,median,mode])

# write calculated results to the output file
write_results_to_file( output_file = 'calculated_results.csv', results = results)

# calculate_median()
# write_results_to_file()