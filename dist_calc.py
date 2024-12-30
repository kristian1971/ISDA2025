
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cosine
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import minkowski
import csv
import numpy as np

data1 = np.genfromtxt("WVS2.csv", encoding=None, dtype=None, delimiter=',') 

with open('llmi3eGPT.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
#print(data2['USA_'])
data2 = np.array(data, ndmin=1, dtype=float)

for row in data1:
    i=cityblock(list(row),data2[0])
    print(i)

