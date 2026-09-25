

import numpy as np

data = np.array([[10, 20],
                 [15, 25],
                 [20, 30]])
mean = data.mean(axis=0)
print(mean)
result = data - mean

