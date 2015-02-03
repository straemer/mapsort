#!/usr/bin/python3

import random
import copy
import timeit

N = 10000000
RANGE = 100000

data = [0]*N

for i in range(N):
    data[i] = random.randrange(0,RANGE)
    if i%(N/100) == 0:
        print(i*100/N)

sorted1 = None
sorted2 = None

m = {}
for i in range(RANGE):
    m[i] = 0

def test1():
    sorted1 = sorted(data)

def test2():
    for i in data:
        m[i] += 1
    sorted2 = []
    for i in range(0, RANGE):
        if i in m:
            sorted2 += [i]*m[i]
print("sorting")
t1 = timeit.timeit("test1()", setup="from __main__ import test1", number=1)
print("t1 = {}".format(t1))
t2 = timeit.timeit("test2()", setup="from __main__ import test2", number=1)
print("t2 = {}".format(t2))

assert(sorted1==sorted2)
