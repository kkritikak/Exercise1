import math
import numpy as np
import matplotlib.pyplot as p
#import gi
#from gi.repository import Gtk

def random_numbers():
    return np.random.uniform()


# 1)
#  a)
a = []
for n in range(100000):
    a.append(random_numbers())

#  b)
def average(x):
    sum = 0.0
    for i in x:
        sum += i
    return sum / len(x)

def variance(x):
    v = 0.0
    a = average(x)
    for i in x:
        v += (i - a)**2
    return v

def err(x):
    return math.sqrt(variance(x) / len(x))

print(average(a), variance(a), err(a))

#  c)
counts, bins = np.histogram(a)
p.hist(counts, bins)
p.plot()

#  d)
b = []
for n in range(100000):
    b.append(random_numbers())

p.scatter(a, b, 0.1)
p.plot()

#  e)
def my_random(seed):
    a = 1664525
    b = 1013904223
    m = 2**32
    x = ((a*seed+b)%m)
    return x / m

c = []
for n in range(100000):
    c.append(my_random(11))

counts, bins = np.histogram(c)
p.hist(counts, bins)
p.plot()

# 2)
n = 2**20
hits = 0
for i in range(n):
    x, y = random_numbers(), random_numbers()
    if (x*x + y*y < 1):
        hits += 1
pi = 4 * hits / n

print(pi)


# 4)
#  a)
# When we reach low temperatures relativly stable areas form.
# By increasing the temperature they diffuse and get random. The transition to randomness is
# found by roundabout T=2.47

#  b)
# 1 random cell selection
# 2 energy calculation: E_i=-J * sum(s_j, s_k)
# 3 energy calculation E_j
# 4 enery calculation of the difference deltaE = H_i - H_j
# 5 flip is accepted if w_ij = min(1, e^(-b*delteE)) else reject flip
# 6 repeat
