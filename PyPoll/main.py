import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

  # candidate_name = str(election_data[2])
	# candidate_votes = int()
	# candidate_percent_votes = int()
	# winning_candidate = str()
 
with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile)
  print(csvreader)
  csv_header = next(csvreader)
    
  print (f"CSV Header: {csv_header}")
  print("_____________________________________")

  # dict={f"Candidate":str[" "], "candidate_votes":int[0], "candidate_percent_votes":float[0]}
  # candidates = {f'str[candidate_name]:int[candidate_votes]: int[candidate_percent_votes]'}
  
  total_votes = 0
  name_count = {}
  # candidate_name = []
  # candidate_votes = 0
  # candidate_percent_votes = [] 
  
  for row in csvreader:
    total_votes = total_votes + 1
    candidate_name = row[2]
    for name in candidate_name:
      if name in name_count:
        name_count[name] += 1
      else:
        name_count[name] = 1
        
        
      # if candidate_name == candidate_name:
      # name_count = candidate_name
      
  print (f"Total votes: ",int(total_votes))
  print (name_count)
  
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
  # candidate_name = ['Candidate'] 
  
  # for row in csvreader:
  #   if (row['Candidate']) != (row['Candidate']):
  #     candidate_name.append
        
        
# column_names=["{csv_header}"]
# dict = {'Ballot ID':[],'County':[], 'Candidate':[]}

# with open(csvpath) as csvfile:
#     dict_object = csv.DictWriter(csvfile, columnnames = column_names)
#     dict_object.writerow(dict)
    
    
    
    # for item in csvreader:
    #   print(item[2])
        
   
      # if (item[2]) == (item[2]):
      #   count = count +1
      #   print(count)
      
    # dict={f"Candidate":str[], "candidate_votes":int[], "candidate_percent_votes":float[]}
    # candidates = {f'str[candidate_name]:int[candidate_votes]: int[candidate_percent_votes]'}
    # candidate_name = []
    # candidate_votes = 0
    # candidate_percent_votes = []
    
    # 
    # for row in csvfile:
    #   if 'Candidate' == 'Candidate':
    #     candidate_votes = candidate_votes + 1
    #     print(f"candidate_votes")
      
    #   candidate_name.append
    #   if 'Candidate' == Candidate:
    #     candidate_votes.append('Candidate")
    #   else: 
    #     candidate_name.append
    # for candidate_name, candidate_votes, candidate_percent_votes in candidates.items():
    #   print(f"{candidate_name} ": " {candidate_percent_votes} " %" {candidate_votes}")
    
    
    #     candidate_votes_count = {}
    #     total_vote_counts =()
        
    # for row in csvfile:
    #     candidate_name = row[2]
    #     if candidate_name not in candidate_votes_count:
    #         candidate_votes_count[candidate_name]=1
    #     else:
    #         candidate_votes_count[candidate_name]+=1
    
    # total_votes=(len(candidate_votes_count{}))  
    # candidate_percent_votes = (f"{total_votes}/{candidate_votes}%"))
        
    #find the candidate_name with the highest candidate_percent_votes
    # winning_candidate = 
        
        
        
    
    # print("Election Results")
        
    # print("_____________________________________")
    
    # print (f"Total votes: ",int(total_votes))
        
    # print("_____________________________________")
    
    # print(f"{candidate_name} : {candidate_percent_votes} {candidate_votes}")
        
    # print("_____________________________________")
        
    # print(f"Winner : {winning_candidate}")
    
   
     
      
        