#import modules
import os
import csv
#set path to csv
budget_csv=os.path.join("Resources/budget_data.csv")
#set up csv reader
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Make lists to later use to manipulate data
    months=[]
    profit_loss=[]
    monthly_change=[]

    next(csvreader)
    #set up data analysis of the csv  
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
    #Find total months
    print("Total Months: ", str(len(months)))
    #Find total profit/loss
    print("Total:$ "+str(sum(profit_loss)))
    #Find average change of profit/loss
    for i in range(len(profit_loss)-1):
        monthly_change.append((profit_loss[i+1]-profit_loss[i]))
    average_monthly_change=sum(monthly_change)/len(monthly_change)
    average_monthly_change=str(round(average_monthly_change,2))
    print("Average Change: "+"$"+str(average_monthly_change))
    #Greatest Increase in Profit/Loss and correspoing month
    max_monthly_change=max(monthly_change)
    index_monthly_change = 0
    for i in range(len(monthly_change)):
        if monthly_change[i]==max_monthly_change:
            index_monthly_change = i
            break

    print("Greatest Increase in Profits: "+months[index_monthly_change+1]+" "+str(max_monthly_change))

    #Greatest Decrease in Profit/Loss and corresponding month
    min_monthly_change=min(monthly_change)
    index_monthly_change=0
    for i in range(len(monthly_change)):
        if monthly_change[i]==min_monthly_change:
            index_monthly_change = i
            break
    
    print("Greatest Decrease in Profits: "+months[index_monthly_change+1]+ " "+str(min_monthly_change))


output_file = os.path.join("Analysis/Financial Results.txt")
with open(output_file, 'w', newline='') as file:
     text = csv.writer(file)
     text.writerow(["Financial Analysis"])
     text.writerow(["-----------------------------------"])
     text.writerow(["Total Months: ",str(len(months))])
     text.writerow(["Total:$ "+str(sum(profit_loss))])
     text.writerow(["Average Change: "+"$"+str(average_monthly_change)])
     text.writerow(["Greatest Increase in Profits: "+months[index_monthly_change+1]+" "+str(max_monthly_change)])
     text.writerow(["Greatest Decrease in Profits: "+months[index_monthly_change+1]+ " "+str(min_monthly_change)])




   
