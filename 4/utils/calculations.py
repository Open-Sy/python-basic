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