import os
import csv

pybank_csv = os.path.join("..", "03-Python_homework_PyBank_Resources_budget_data.csv")

months = []
profit = []
avg = []
change = []
prev = 0

csvfile = open(pybank_csv, 'r')
textfile = open("PyBank.txt", "w")


csvreader = csv.reader(csvfile, delimiter=",")
header = next(csvreader)
for row in csvreader:
    months.append(row[0])
    profit.append(int(row[1]))
    curr = int(row[1])
    val1 = curr - prev
    change.append(val1)
    prev = curr

avg_change = round(sum(change[1:])/len(change[1:]), 2)

date_len = len(months)
net_total = sum(profit)

height = max(profit)
floor = min(profit)
max_index = profit.index(height)
min_index = profit.index(floor)
max_month = months[max_index]
min_month = months[min_index]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {date_len}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_month} (${height})")
print(f"Greatest Decrease in Profits: {min_month} (${floor})")

out_put = os.path.join("PyBank.txt")

textfile.write("Financial Analysis\n")
textfile.write("----------------------------\n")
textfile.write(f"Total Months: {date_len}\n")
textfile.write(f"Total: ${net_total}\n")
textfile.write(f"Average Change: ${avg_change}\n")
textfile.write(f"Greatest Increase in Profits: {max_month}:(${height})\n")
textfile.write(f"Greatest Decrease in Profits: {min_month} (${floor})\n")

csvfile.close()
textfile.close()
