import csv
filename = 'data/weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)
 # Get high temperatures from this file.
highs = []
for row in reader:
  high = int(row[5])
highs.append(high)
print(highs)