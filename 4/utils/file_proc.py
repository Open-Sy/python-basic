import csv

def write_results_to_file(output_file, results):
    '''
    write calculate results to the file
    '''
    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(results)