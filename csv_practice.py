import csv

DATA_PATH = '/학부인턴/자료/'

csvFile = open(DATA_PATH + "text_data.csv", 'w+')

try:
    writer = csv.writer(csvFile)
    writer.writerow(('testing',))

    for i in range(3):
        writer.writerow((str(i)))
finally:
    csvFile.close()