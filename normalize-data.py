import csv

rawData=[]

with open("csvs/hsi-price-2021-09.csv") as f:
  for l in csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
    rawData.append(l)

print(rawData)

# for date in data:


foo = numpy.unique(rawData, 0)

print(foo)