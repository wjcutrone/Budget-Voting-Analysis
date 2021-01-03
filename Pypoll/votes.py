#import modules
import os
import csv


def num():
  filename=os.path.join("./Resources/"+"voting_data.csv")
  count = 0;

  with open(filename,'r') as csvfile:
    for line in csvfile:
         count  += 1
  csvfile.close()
  return count

#total = num()
#print("Total Votes:",total)   
