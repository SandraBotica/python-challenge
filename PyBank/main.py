    #import os module
import os
    #import module for reading csv files
import csv
    #path to collect data where the csv file is
csvpath = os.path.join('Resources', 'budget_data.csv')

    
	#Assign values to variables
total_number_months = 0
net_total_amount = 0
last = None
last2 = None
date = []
monthly_change = []
greatest_increase_profits = ()
greatest_decrease_profits = ()

    # opens path to where the file stream is <> for the csv file
with open(csvpath, newline='') as csvfile:
        # pass the file stream <> into the csv DictReader specifying the delimiter
    csvreader = csv.DictReader (csvfile, delimiter=',')
    print(csvreader)
        # read each row of data after the header and you can do something with it in the for loop    
    for row in csvreader:
        total_number_months = total_number_months + 1
        net_total_amount = net_total_amount + int(row['Profit/Losses'])
        if last is not None:
            monthly_change.append(int(row['Profit/Losses'])-last)
            date.append(row['Date'])
        last = int(row['Profit/Losses'])      
    greatest_increase_profits = max(monthly_change)  
    greatest_decrease_profits = min(monthly_change)  
    average_monthly_change = sum(monthly_change)/len(monthly_change)
        
print("Financial Analysis")
print("_____________________________________")
print(f"Total months: ",int(total_number_months))
print(f"Total: $ ",int(net_total_amount)) 
print (f"Average change: $ {round(average_monthly_change, 2)}")
print (f"Greatest Increase in profits : $ {greatest_increase_profits}")
print (f"Greatest Decrease in profits : $ {greatest_decrease_profits}")
    
    # print (f"Greatest Increase in profits : {date} ($ int{greatest_increase-profits})")
    # print (f"Greatest Decrease in profits : {date} ($ int{greatest_decrease-profits})")

output_file = os.path.join("analysis", "PyBank.txt")
with open(output_file, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["_____________________________________"])
    writer.writerow([f"Total months: ",int(total_number_months)])
    writer.writerow([f"Total: $ ",int(net_total_amount)])
    writer.writerow([f"Average change: $ {round(average_monthly_change, 2)}"])
    writer.writerow([f"Greatest Increase in profits : $ {greatest_increase_profits}"])
    writer.writerow([f"Greatest Decrease in profits : $ {greatest_decrease_profits}"])
    
    # with open(csvpath) as csvfile:
        # csvreader = csv.reader (csvfile, delimiter= ",")
        # print(csvreader)
        # csv_header = next(csvreader)
        # print (f"CSV Header: {csv_header}")
    
    # for item in csvreader:
        # print(item [0], item[1])
    
    # for row in csvreader:
        # total_number_months = total_number_months + 1
        # net_total_amount = net_total_amount + int(row[1])
            # if last is not None:
                # monthly_change.append(int(row[1])-last)
                # date.append(row[0])
            # last = int(row[1])      
    # greatest_increase_profits = max(monthly_change)   
    # greatest_decrease_profits = min(monthly_change) 
    # average_monthly_change = sum(monthly_change)/len(monthly_change)
    
    # print (f"Total months: ", int(total_number_months))
    # print(f"Total: $ ",int(net_total_amount)) 
    # print (f"Average change: $ {round(average_monthly_change, 2)}")
    # print (f"Greatest Increase in profits : $ {greatest_increase_profits}")
    # print (f"Greatest Decrease in profits : $ {greatest_decrease_profits}")
    
    
    # total_number_months = 0
    # monthly_amount = []
    # net_total_amount = 0
    # monthly_change = {}
    # lines = csvfile.readlines()
    # output =[0]
    # header = lines[0]
    # data = [int('Profit/Losses') for number in lines[1:]]

    # for index, number in enumerate(data[1:],1): 
        # output.append(int('Profit/Losses')- data[index-1]) 
        # print(output)     
        # monthly_change = row['Date'] = row['Profit/Losses'] - (lines[index - 1][row['Profit/Losses']])
    
    # for row in csvreader:  
        # total_number_months = total_number_months + 1
        # net_total_amount = net_total_amount + int(row['Profit/Losses'])
    
    
    # print("Financial Analysis")
    # print("_____________________________________")
    # print (f"Total months: ", int(total_number_months))
    # print(f"Total: $ ", int(net_total_amount))
    # print(monthly_change)
    
    
    # budgetData = list(csvreader)
    
    # net_total_amount = 0
    
    # for row in csvreader:
        # net_total_amount = net_total_amount + next(budgetData[0][1])
    
    # date =
    # increase_profits = 0  how to obtain first positive value in column monthly change
    # greatest_increase_in_profits ={}
    # greatest_increase_in_profits ={"Date": "amount"}
    # for row in csvreader:
        # if (monthly_change) is >0 and > increase_profits:
            # append.increase_profits with monthly_change and append.date
            # greatest_increase_profits = (increase_profits)
        # else:
        
    # date =
    # decrease_profits = 0  how to obtain first negative value in column monthly change
    # greatest_decrease_in_profits ={}
    # greatest_decrease_in_profits ={"Date": "amount"}
    # for row in csvreader:
        # if (monthly_change) is <0 and > decrease_profits:
            # append.decrease_profits with monthly_change and append.date
            # greatest_decrease_profits = (decrease_profits)
        # else:
    
    # net_total_amount = []
    # profits = []
    # losses = []
    # for row in csvreader:  
    #     for item in csvreader:
    #         amount =int(item[1])
    #         if amount > 0:
    #             profits.append
    #         else:
    #             losses.append
    # print(profits) 
    # print(losses)
      
    # print("Financial Analysis")
        
    # print("_____________________________________")
      
    # print (f"Total months: ", int(total_number_months))
    
    # print(f"Total: $ ", int(net_total_amount))
    
    # print (f"Average change: $ {round(average_monthly_change, 2)}")

    # print (f"Greatest Increase in profits : {date} ($ int{greatest_increase-profits})")
    
    # print (f"Greatest Decrease in profits : {date} ($ int{greatest_decrease-profits})")