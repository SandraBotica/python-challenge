import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

    
    # net_total_amount = int(budget_data[1])
    # date =str(budget_data[0])
    # monthly_change = int
    # average_monthly_change = int({monthly_change}/{total_number_months})
    # increase_profits = int     
    # greatest_increase_profits = int
    # decrease_profits = int     
    # greatest_decrease_profits = int
    
# with open(csvpath) as csvfile:
#     csvreader = csv.reader (csvfile)
#     print(csvreader)
#     csv_header = next(csvreader)
    
#     print (f"CSV Header: {csv_header}")
    
#     # for item in csvreader:
#     #     print(item [0], item[1])
    
#     total_number_months = 0
    
#     for row in csvreader:
#         total_number_months = total_number_months + 1
#     print (f"Total months: ", int(total_number_months))
    
with open(csvpath, newline='') as csvfile:
    csvreader = csv.DictReader (csvfile, delimiter=',')
    
    total_number_months = 0
    # monthly_amount = []
    net_total_amount = 0
    # monthly_change = {}
    # lines = csvfile.readlines()
    
    for row in csvreader:
        
        total_number_months = total_number_months + 1
        net_total_amount = net_total_amount + int(row['Profit/Losses'])
    
    print("Financial Analysis")
    print("_____________________________________")
    print (f"Total months: ", int(total_number_months))
    print(f"Total: $ ", int(net_total_amount))
           
    # for index, line in enumerate(lines[1:]):       
    #         monthly_change = row['Date'] = row['Profit/Losses'] - (lines[index - 1][row['Profit/Losses']])
    
    # print("Financial Analysis")
    # print("_____________________________________")
    # print (f"Total months: ", int(total_number_months))
    # print(f"Total: $ ", int(net_total_amount))
    # print(monthly_change)
    
    
    # budgetData = list(csvreader)
    
    # net_total_amount = 0
    
    # for row in csvreader:
    #     net_total_amount = net_total_amount + next(budgetData[0][1])
        
    
    # monthly_change = 
    # should we be writing this into the csv i.e. row[1] add to next row
    # save this value 
    # average_monthly_change = int({monthly_change}/{total_number_months})
    
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
    
    # print (f"Average change: $ int{average_monthly_change}")
    
    # print (f"Greatest Increase in profits : {date} ($ int{greatest_increase-profits})")
    
    # print (f"Greatest Decrease in profits : {date} ($ int{greatest_decrease-profits})")