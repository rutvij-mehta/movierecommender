import csv

length = 0
with open('ratings.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {int(rows[0]):[int(rows[1]),float(rows[2])] for rows in reader}
    print(mydict)
    length = len(mydict)
