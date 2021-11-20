# Zadanie 23

import csv

with open('files/students.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for pos, row in enumerate(spamreader):
        if pos > 0:
            print(row[0] + "   " + row[1] + "   " + row[4])