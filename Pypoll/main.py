#import modules
import votes
import candidates
import os
import csv

total = votes.num()
print("Total Votes:",total)   

candidates_list=candidates.names()
i=0
j=0
votes_per_candidate=[]
for i in candidates_list:
      votes_per_candidate.append(0)
# print list 
print("Candidates List:")
candidates_list.pop(0)
for x in candidates_list: 
      print (x,":"); 
voting_csv=os.path.join("./Resources/voting_data.csv")
with open(voting_csv) as csvfile:
    
    for line in csvfile:
      line=line.strip("\n")
      fields = line.split(",") 
      i=0

      for candidate in candidates_list:
            if fields[2]==candidate:
                  
                  votes_per_candidate[i]=votes_per_candidate[i]+1
                  
            i=i+1
    j=0
    max=0
    winner= " "
    #print(votes_per_candidate[0])
    for candidate in candidates_list:
            print(candidate,":","%.3f" %round(votes_per_candidate[j]/total*100), "%","(",votes_per_candidate[j],")")
            if max<votes_per_candidate[j]:
                  max=votes_per_candidate[j]
                  winner=candidate
            j=j+1
print("The winner of the election by popular vote: ",winner)
csvfile.close     
