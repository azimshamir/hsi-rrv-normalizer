import numpy
import csv
import functools

def cleanF(n):
  return float(n.strip().replace(",", ""))

def readFile(url):
  rawData=[]

  with open(url) as f:
    for l in csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
      rawData.append(l)

  return rawData

def writeFile(url, outputFile, fullWriter):
  with open(url, 'w', encoding='UTF8') as outputFile:
    writer = csv.writer(outputFile)
    

    writer.writerow(['date', 'high', 'low'])
    for point in ouputData:
      writer.writerow(point)
      fullWriter.writerow(point)

def getDates(arr):
  def flatten(x):
      return x[0]

  allDates=list(map(flatten, rawData))

  return numpy.unique(allDates)

def getHighsAndLows(date):
  def pickMaxHigh(acc, dataPoint):
    val=cleanF(dataPoint[7])

    if dataPoint[0] != date:
      return acc

    if val > acc:
      return float(val)
    else:
      return acc

  def pickMinLow(acc, dataPoint):
    val=cleanF(dataPoint[6])
    
    if dataPoint[0] != date:
      return acc

    if val < acc:
      return float(val)
    else:
      return acc

  maxHigh=functools.reduce(pickMaxHigh, rawData, 0)
  minLow=functools.reduce(pickMinLow, rawData, 999999999999999)

  return [date, maxHigh, minLow]

files=[
  "hsi-price-2021-09.csv",
  "hsi-price-2021-10.csv",
  "hsi-price-2021-11.csv",
  "hsi-price-2021-12.csv",
  "hsi-price-2022-01.csv",
  "hsi-price-2022-02.csv",
]


with open("output/full-output.csv", 'w', encoding='UTF8') as fullOutputFile:
  fullWriter = csv.writer(fullOutputFile)

  fullWriter.writerow(['date', 'high', 'low'])

  for file in files:  
    rawData = readFile("csvs/"+file)
    dates = getDates(rawData)
    ouputData=list(map(getHighsAndLows, dates))
    writeFile('output/'+file, ouputData, fullWriter)