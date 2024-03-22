#Import Data
import os
import csv

# Open and read csv
cereal_csv = os.path.join("..", "Resources", "budget_data.csv")

#Output of csv file into text
cereal_csv_path = "output.text"

#Set ResuLts to Print in Correctly Terminal
Total_Months = ()
Total = ()
Average_Change = ()
Greatest_Increase = ()
Greatest_Decrease = ()
Change_Profit = ()

#Open csv file data
with open(budget_data) as csvfile:
    csvreader = (budget_data)

Total_months = sum("Date")
Print(Total_months)

Total = sum("Profit/Losses")
Print(Total)

Average_Change = mean("Profit/Loses")
Print(Average_Change)

Greatest_Increase = max("Profits/Losses")
Print(Greatest_Increase)

Greates_Decrease = min("Profits/Losses")
Print(Greatest_Decrease)

Change_Profit = (Greatest_Increase - Greatest_Decrease)
Print(Change_Profit)







