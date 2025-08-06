#!/usr/bin/env python3

for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    
    print("Range:", i)