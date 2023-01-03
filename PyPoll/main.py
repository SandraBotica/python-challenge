  # import os module
import os
  # import module for reading csv files
import csv
  # path to collect data where the csv file is
csvpath = os.path.join('Resources', 'election_data.csv')

  # Assign values to variables
count = 0
candidate_name = []
candidate_votes = []
dictionary = {}
candidate_percent_votes = []
winning_candidate = 0

  # opens path to where the file stream is <> for the csv file
with open(csvpath) as csvfile:
  # pass the file stream <> into the csv reader specifying the delimiter
  csvreader = csv.reader(csvfile, delimiter=",")
  print(csvreader)
  csv_header = next(csvreader)
    
  # print (f"CSV Header: {csv_header}")
  # print("_____________________________________")
  
    # read each row of data after the header and you can do something with it in the for loop    
  for row in csvreader:
    count = count + 1
    if row[2] not in candidate_name:
      candidate_name.append(row[2])
    candidate_votes.append(row[2])
        
for name in candidate_votes:
    dictionary [name] = dictionary.get(name,0) + 1

total_votes = list(dictionary.values())

for percent in total_votes:
  candidate_percent_votes.append(round((percent/count)*100,3))
  
percent_votes = [f"{votes}%" for votes in candidate_percent_votes] 
candidate_names = [f"{names}" for names in candidate_name] 
summary = zip(candidate_names,percent_votes,total_votes)
winning_candidate = max(total_votes)
index = total_votes.index(winning_candidate)
length = len(total_votes)
winner = candidate_name[index]


print("Election Results")    
print("_____________________________________")
print()
print (f"Total votes: {count}")
print("_____________________________________")
print()
for entry in summary:
  print(entry)
print("_____________________________________")
print()
print(f"Winner: {winner}")
print("_____________________________________")

output_file = os.path.join("analysis", "PyPoll.txt")
with open(output_file, 'w') as file:
    writer = csv.writer(file)
    writer.writerow([])
    writer.writerow(["Election Results"])
    writer.writerow(["_____________________________________"])
    writer.writerow([])
    writer.writerow([f"Total votes: {count}"])
    writer.writerow(["_____________________________________"])
    writer.writerow([])
    writer.writerows([entry])
    writer.writerow(["_____________________________________"])
    writer.writerow([])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["_____________________________________"])
   
   
       
  # for item in csvreader:
  #   print(item[2])
        
  # if (item[2]) == (item[2]):
  #   count = count +1
  #   print(count)

  # name_count = {}
  # dict={f"Candidate":str[" "], "candidate_votes":int[0], "candidate_percent_votes":float[0]}
  # candidates = {f'str[candidate_name]:int[candidate_votes]: int[candidate_percent_votes]'}
  

  # for item in csvreader:
  #     print (item[2])
    
  # for row[2] in csvreader:
  #   if 'Candidate' == 'Candidate':
  #     candidate_votes = candidate_votes + 1
  # print(f"['candidate_name'], int[candidate_votes]")
  
  #   candidate_name.append
  #   if 'Candidate' == Candidate:
  #     candidate_votes.append('Candidate")
  #   else: 
  #     candidate_name.append
  
  # for candidate_name, candidate_votes, candidate_percent_votes in candidates.items():
  #   print(f"{candidate_name} ": " {candidate_percent_votes} " %" {candidate_votes}")
    
    

  # with open(csvpath, newline='') as csvfile:
  #   csvreader = csv.DictReader (csvfile, delimiter=',')
  
  #   column_names=["{csv_header}"]
  #   dict ={}
  #   poll = {'Ballot ID':[],'County':[], 'Candidate':[]}
   
  #   for Candidate in poll:
  #     candidate_name = poll[Candidate]
  #     print (candidate_name)
  #   candidate_name = ['Candidate'] 
  
  # for row in csvreader:
  #   if (row['Candidate']) != (row['Candidate']):
  #     candidate_name.append
          
          
  # column_names=["{csv_header}"]
  # dict = {'Ballot ID':[],'County':[], 'Candidate':[]}

  # with open(csvpath) as csvfile:
  #     dict_object = csv.DictWriter(csvfile, columnnames = column_names)
  #     dict_object.writerow(dict)
      
  # dict={f"Candidate":str[], "candidate_votes":int[], "candidate_percent_votes":float[]}
  # candidates = {f'str[candidate_name]:int[candidate_votes]: int[candidate_percent_votes]'}
  # candidate_name = []
  # candidate_votes = 0
  # candidate_percent_votes = []
  # candidate_votes_count = {}
  # total_vote_counts =()
        
  # for row in csvfile:
  # candidate_name = row[2]
  #     if candidate_name not in candidate_votes_count:
  #         candidate_votes_count[candidate_name]=1
  #     else:
  #         candidate_votes_count[candidate_name]+=1
    
  # total_votes=(len(candidate_votes_count{}))  
  # candidate_percent_votes = (f"{total_votes}/{candidate_votes}%"))
        
   #find the candidate_name with the highest candidate_percent_votes
  # winning_candidate = 
  
   
     
      
        