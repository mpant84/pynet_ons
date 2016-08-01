#!/usr/bin/env python


f1 = open("exercise5_1.txt")

for line in f1:
  print line.strip()

f1.close()

f2 = open("exercise5_2.txt","w")
f2.write("test string\n")
f2.close()

with open("exercise5_2.txt","a") as f:
  f.write("appending\n")
   
