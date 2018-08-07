import os
import csv
def read_from_csv (csv_filename):
    """
    this function will read a csv file and return a list of best houses

    :param csv_filename: csv.filename

    :return: list of houses

    """
    fields = []
    rows = []
    with open(csv_filename,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.next()
        for row in csvreader:
            rows.append(row)
    return fields , rows


#testing

fields, rows = read_from_csv("redfin-favorites.csv")

print (rows[0][3])
