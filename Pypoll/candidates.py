#import modules
import os
import csv


def names():
  filename=os.path.join("./Resources/"+"voting_data.csv")

 
  names_list = [] 
  numvotes_list = []
  fields = [ ] 

  with open(filename,'r') as csvfile:
    for line in csvfile:
      line = line.strip("\n")
      fields = line.split(",")
      if fields[2] not in names_list: 
         names_list.append(fields[2]) 
         
  csvfile.close();
  return names_list




#candidates_list=names()
# print list 
#print("Candidates List:")
#candidates_list.pop(0)
#for x in candidates_list: 
      #print (x," "); 

