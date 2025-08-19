import numpy as np
import csv

with open("../../../pythontesting/usage-data.csv", mode="r") as f:
    reader = csv.reader(f)
    first_row = next(reader)
    usage_data = np.array([
        first_row
    ], np.uint16)
    print(usage_data.ndim)
    for row in reader:
        usage_data = np.append(usage_data, [row], axis=0)
    print(usage_data)
