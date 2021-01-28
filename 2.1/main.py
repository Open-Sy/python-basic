import csv

# function from files import 
from utils.calculations import calculate_mean, calculate_median, calculate_mode
from utils.file_proc import write_results_to_file


if __name__ == '__main__': 

    # initialize variables
    results = []
    output_file = 'data/outputs/calculated_results.csv'

    # read the input file
    with open('data/inputs/data.csv','r', newline='\n') as f:
        raw_data = csv.reader(f)
        data = [i for i in raw_data]

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
    write_results_to_file( output_file , results)