import csv

def convert_csv_to_tsv(input_file='../ds.csv', output_file='ds.tsv'):
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        with open(output_file, 'w', newline='', encoding='utf-8') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            for row in reader:
                writer.writerow(row)

if __name__ == '__main__':
    convert_csv_to_tsv()
