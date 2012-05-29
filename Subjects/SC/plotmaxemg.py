import matplotlib.pyplot as plt
import csv
import numpy as np

with open('SC_maxEMG.csv') as f:
    reader = csv.reader(f, delimiter=",")
    header = reader.next()
    data = np.array([[float(col) for col in row] for row in reader])


for idx, name in enumerate( header[1:] ):
    plt.plot(data[:,idx+1])

plt.show()