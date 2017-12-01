#!/bin/python

import sys

result = 0
n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
for i in xrange(n):
            result += a[i][i]
            result -= a[i][n-i-1]      
print abs(result)
