#!/bin/python3

import os
import sys

#
# Complete the componentsInGraph function below.
#
def find(i, root):
    while i != root[i]:
        i = root[i]
    return i

def union(x, y, root, count):
    if x != y:
        root[y] = x
        count[x] += count[y]
        count[y] = 0
    return root, count

n = int(input())
root = [i for i in range(2*n+1)]
count = [1 for i in range(2*n+1)]
for i in range(n):
    inp = list(map(int, input().split()))
    x = find(inp[0]-1, root)
    y = find(inp[1]-1, root)
    root, count = union(x, y, root, count)
mincount = 2*n+1
maxcount = 0
for i in range(2*n+1):
    if count[i] > 1 and count[i] < mincount:
        mincount = count[i]
    if count[i] > maxcount:
        maxcount = count[i]
print(mincount, maxcount)