import numpy as np
import matplotlib.pyplot as plt

k1 = 0.18
k2 = 0.35
c1 = 1
c2 = 1.2
tt = 100
t = np.array([0, 2, 4, 6, 8, 10])


def m_calc(p1, b, k):
    P = 3.5
    p2 = P - p1
    Wp = (k1 * p1 + k2 * p2) * 8760
    Wo = P * 8760 * b
    Wi = Wo - Wp
    C = 10 ** 6 * (p1 * c1 + p2 * c2) + 1000000
    M = - C - Wi * tt * t + Wo * (tt + k) * t
    roi = (- Wi * tt * t + Wo * (tt + k) * t) / C
    return M, roi


m1, roi1 = m_calc(0, 0.2, 5)
m2, roi2 = m_calc(0, 0.2, 20)
m3, roi3 = m_calc(0, 0.5, 5)
m4, roi4 = m_calc(0, 0.5, 20)
m5, roi5 = m_calc(3.5, 0.2, 5)
m6, roi6 = m_calc(3.5, 0.2, 20)
m7, roi7 = m_calc(3.5, 0.5, 5)
m8, roi8 = m_calc(3.5, 0.5, 20)


# First figure
plt.figure(1)
plt.title('Revenue over time')
plt.plot(t, m1, label='p1 = 0, b = 0.2, k = 5')
plt.plot(t, m2, label='p1 = 0, b = 0.2, k = 20')
plt.plot(t, m3, label='p1 = 0, b = 0.5, k = 5')
plt.plot(t, m4, label='p1 = 0, b = 0.5, k = 20')
plt.plot(t, m5, label='p1 = 3.5, b = 0.2, k = 5')
plt.plot(t, m6, label='p1 = 3.5, b = 0.2, k = 20')
plt.plot(t, m7, label='p1 = 3.5, b = 0.5, k = 5')
plt.plot(t, m8, label='p1 = 3.5, b = 0.5, k = 20')

plt.xlabel("Years")
plt.ylabel("Revenue")

plt.legend()


# Second figure
plt.figure(2)
plt.title('ROI over time')
plt.plot(t, roi1, label='roi1')
plt.plot(t, roi2, label='roi2')
plt.plot(t, roi3, label='roi3')
plt.plot(t, roi4, label='roi4')
plt.plot(t, roi5, label='roi5')
plt.plot(t, roi6, label='roi6')
plt.plot(t, roi7, label='roi7')
plt.plot(t, roi8, label='roi8')

plt.xlabel("Years")
plt.ylabel("ROI")

plt.legend()
plt.show()