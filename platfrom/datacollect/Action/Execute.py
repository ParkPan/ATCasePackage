#!/usr/bin/python
import sys


filename = sys.argv[1] + ".txt"
inputfile = open(filename, "r")
severlog = open("/home/test/TestInput/input.log", "a")
count = 0
for eachline in inputfile:
    severlog.write(eachline)
    count += 1
severlog.close()
inputfile.close()
print "input " + str(count) + "logs"
print "script execute finish"
