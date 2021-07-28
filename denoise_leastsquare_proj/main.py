import os
import numpy as np
import matplotlib.pyplot as plt

data = np.load('btc_price.npy')
if not os.path.exists("lambda"):
    os.makedirs("lambda")

i = np.identity(2500)
d = -np.eye(2499, 2500)
d = np.roll(d, 1)
d2 = np.eye(2499, 2500)
d3 = d2 + d

d = np.transpose(d3).dot(d3)
for lambdaa in [1000, 3000, 5000, 8000, 10000, 40000, 80000, 100000]:
    data2 = np.linalg.solve(i + lambdaa * d, data)
    plt.plot(data2, color="#8e7618")
    plt.legend(["lambda=" + str(lambdaa)])
    plt.savefig(r"lambda\labmda_" + str(lambdaa))
    plt.show()
