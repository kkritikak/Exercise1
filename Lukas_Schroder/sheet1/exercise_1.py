

from random import random
from math import sqrt
from numpy import histogram
from time import time

#(5/5points for Task 1)
import matplotlib.pyplot as plt

num_values = 100000
num_bins = 100
filename = "100k_random_numbers.txt"

def task_1_a ():
    file = open(filename, "w", encoding="utf-8")
    for _ in range(num_values):
        file.write(str(random())+"\n")
    file.close()
    

def task_1_b ():
    file = open(filename, "r", encoding="utf-8")
    mean = 0
    variance = 0
    num_lines = sum(1 for _ in file)
    file.seek(0)
    for _ in range(num_lines):
        value = float(file.readline().rstrip())
        mean += value/num_lines
    file.seek(0)
    for _ in range(num_lines):
        value = float(file.readline().rstrip())
        variance += ((value - mean)**2) / num_lines
    file.close()
    error = sqrt(variance/num_values)

    return (mean, variance, error)

def task_1_c ():
    values = []
    file = open(filename, "r", encoding="utf-8")
    num_lines = sum(1 for _ in file)
    file.seek(0)
    for _ in range(num_lines):
        values.append(float(file.readline().rstrip()))
    file.close
    hist, _ = histogram(a=values, bins=num_bins)

    plt.bar(x=range(num_bins), height=hist)
    plt.xlabel("buckets")
    plt.ylabel("number of random values")
    plt.show()

    return hist

def task_1_d ():
    x_values = []
    y_values = []
    for _ in range(num_values):
        x_values.append(random())
        y_values.append(random())
    plt.plot(x_values, y_values)
    plt.show()

    return x_values, y_values

def task_1_e (num_values=1, seed=round(time() * 1000)):
    a = 1664525
    c = 1013904223
    m = 2e32
    x = seed
    xs = []

    for _ in range(num_values):
        x = (a * x + c) % m
        xs.append(x/m)

    return xs
    
if __name__ == "__main__":
    task_1_a()
    task_1_b()
    task_1_c()
    task_1_d()
    task_1_e()
    