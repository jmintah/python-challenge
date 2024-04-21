import os
import csv

budget_data = os.path.join("/Users/jayp/Downloads/CU-VIRT-DATA-PT-02-2024-U-LOLC/03-Python/Starter_Code/PyBank/Resources/budget_data.csv")

total_months_budget_data = 0
total_money = 0
value_of_numbers = 0
change_in_average = 0
dates = []
profits_of_change = []

with open(budget_data, newline - "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter - ",")

    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_money += int(first_row[1])
    value_of_numbers = int(first_row[1])

    for row in csvreader:
        dates.append(row[0])

        change = int(row[1])-value_of_numbers
        profits_of_change.append(change_in_average)
        value_of_numbers = int(row[1])

        total_months_budget_data += 1

        total_months_budget_data = total_months_budget_data + int(row[1])

        greatest_increase_data = max(profits_of_change)
        greatest_index_data = profits.index(greatest_increase_data)
        greatest_data_data = dates[greatest_index_data]

        greatest_decrease_data = min(profits_of_change)
        worst_index = profits.index(greatest_increase_data)
        worst_date = dates[worst_index]

        change_in_average = sum(profits)/len(profits)

        print("Financial Analysis")
        print("-----------------------")
        print(f"Total Months: {str(total_months_budget_data)}")
        print(f"Total: ${str(total_months_budget_data)}")
        print(f"Average Change: ${str(round(change_in_average,2))}")
        print(f"Greatest Increase in Profits: {greatest_data_data} (${str(greatest_increase_data)})")
        print(f"Greatest Decrease In Profits: {worst_date} (${str(greatest_decrease_data)})")

        output = open("output.txt", "w")

        line1 = "Financial Analysis"
        line2 = "-----------------------"
        line3 = str(f"Total Months {str(total_months_budget_data)}")
        line4 = str(f"Total: ${str(total_money)}")
        line5 = str(f"Average Change: ${str(round(change_in_average,2))}")
        line6 = str(f"Greatest Increase in Profits: {greatest_data_data} (${str(greatest_increase_data)})")
        line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease_data)})")
        output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
