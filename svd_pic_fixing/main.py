import matplotlib.pyplot as plt
import numpy as np

s = plt.imread(r"images\3.bmp")
r = s[:, :, 0]
g = s[:, :, 1]
b = s[:, :, 2]
for k in [10, 50, 150, 250]:
    u, sig, v = np.linalg.svd(b)
    u = u[:, 0:k]
    sig = sig[0:k]
    new = np.diag(sig)
    v = v[0:k, ]
    q = u.dot(new)
    p = q.dot(v)

    u1, sig1, v1 = np.linalg.svd(g)
    u1 = u1[:, 0:k]
    sig1 = sig1[0:k]
    new1 = np.diag(sig1)
    v1 = v1[0:k, ]
    q1 = u1.dot(new1)
    p1 = q1.dot(v1)

    u2, sig2, v2 = np.linalg.svd(r)
    u2 = u2[:, 0:k]
    sig2 = sig2[0:k]
    new2 = np.diag(sig2)
    v2 = v2[0:k, ]
    q2 = u2.dot(new2)
    p2 = q2.dot(v2)

    a2 = np.dstack((p2, p1, p)).astype(np.uint8)

    plt.imshow(a2)
    plt.savefig(r"photos\k_bmp3_" + str(k))
    plt.show()
