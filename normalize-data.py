import csv

data=[]

with open("csvs/hsi-price-2021-09.csv") as f:
  for l in csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
    data.append(l)

print(data)
