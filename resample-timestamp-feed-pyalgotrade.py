#!/usr/bin/env python3

import csv
import sys
import time

if len(sys.argv) < 2:
    print('Usage: {} [csv]'.format(sys.argv[0]))
    exit(1)

fileWrite = open('out.csv', 'w')
writer = csv.writer(fileWrite)
writer.writerow(['Timestamp', 'Price', 'Amount', 'Side'])

fileRead = open(sys.argv[1], 'r')
reader = csv.reader(fileRead)
for row in reader:
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(row[1][:-3])))
    writer.writerow([timestamp, row[2], row[3], row[4]])

fileWrite.close()
fileRead.close()
