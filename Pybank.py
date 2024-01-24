# defining path for csv file
import os
import csv

# assigning path to open the csv file
csv_import = os.path.join( 'Resources' , 'budget_data.csv')

month=[]
profit=[]
profit_change=[]
monthly_change = []

# using with open statement to read csv
with open(csv_import) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    # skipping header so that it is not included in our analysis as these are headings
    csv_header = next(csv_reader)
    print(csv_reader)

    #for row in csv_reader:
       # print(row)
    
    for row in csv_reader:
        month.append(row[0])
       # print(month)
        print(len(month))

        profit.append(row[1])
        #print(profit_Loss)

    
    profit_int = map(int,profit)
    # calculating total profit
    total_profit = (sum(profit_int))
    print(total_profit)

    # calculating montly change : ( Total of column 2 / total number )
    i = 0
    for i in range(len(profit) - 1):
        profit_loss = int(profit[i+1]) - int(profit[i])
        profit_change.append(profit_loss)
    Total = sum(profit_change)
    monthly_change = Total / len(profit_change)
    print(monthly_change)
    
    # calculating profit increase per month
    profit_increase = max(profit_change)
    print(profit_increase)
    k = profit_change.index(profit_increase)
    month_increase = month[k+1]

    # calculating profit decrease per month
    profit_decrease = min(profit_change)
    print(profit_decrease)
    j = profit_change.index(profit_decrease)
    month_decrease = month[j+1]

# using print statement to print Financial Analysis on terminal
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')
print("Total number of months: " + str(len(month)))
print("Total Revenue in period: $ " + str(total_profit))     
print("Average monthly change in Revenue : $" + str(monthly_change))
print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")
        
        
# creating a text file and adding the results to the text file
with open('Pybank_analysis.txt', "w" ) as text:

    text.write(f'Financial Analysis'+'\n')
    text.write(f'----------------------------'+'\n')
    text.write("Total number of months: " + str(len(month)))
    text.write(f'\n')
    text.write("Total Revenue in period: $ " + str(total_profit)) 
    text.write(f'\n')
    text.write("Average monthly change in Revenue : $" + str(monthly_change))
    text.write(f'\n')
    text.write(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
    text.write(f'\n')
    text.write(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")
