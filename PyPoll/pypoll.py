# defining path for csv file
import os
import csv

# assigning path to open the csv file
csv_import = os.path.join( 'Resources' , 'election_data.csv')

#Ballot ID,County,Candidate
ballot_id=[]
county=[]
candidate_ls=[]

Charles =[]
Diana =[]
Raymon =[]


# using with open statement to read csv
with open(csv_import) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    # skipping header so that it is not included in our analysis as these are headings
    csv_header = next(csv_reader)
    print(csv_reader)

    total_profit= 0 
    for row in csv_reader:
        ballot_id.append(row[0])
        #print(ballot_id)
        county.append(row[1])
        candidate_ls.append(row[2])
        
        
    total_vote = len(ballot_id)
    print(total_vote)
    

    for candidate in candidate_ls:
        if str(candidate) == "Charles Casper Stockham":
            Charles.append(candidate)
            Charles_votes=len(Charles)
        elif candidate == "Diana DeGette":
            Diana.append(candidate)
            Diana_votes = len(Diana)
        else:
            Raymon.append(candidate)
            Raymon_votes= len(Raymon)

    

    print(f'Charles votes : {Charles_votes} , Diana votes : {Diana_votes} ,Raymon votes : {Raymon_votes}')

    
    charles_per= round((Charles_votes/total_vote)*100,3)
    #print(charles_per)
    diana_per= round((Diana_votes/total_vote)*100,3)
    #print(diana_per)
    raymon_per= round((Raymon_votes/total_vote)*100,3)
    #print(raymon_per)

    x= max(Charles_votes,Diana_votes,Raymon_votes)
    #print(x)

    if Charles_votes >= x:
        election_winner = "Charles Casper Stockham"
    elif Diana_votes >= x:
        election_winner = "Diana DeGette"
    else:
        election_winner= "Raymon Anthony Doane"
    
    #print(election_winner)
        
print(f'Election Results'+'\n')
print(f'----------------------------'+'\n')
print("Total Votes: " + str(total_vote))
print(f'----------------------------'+'\n')     
print(f"Charles Casper Stockham :" +str(charles_per) +" % ("+ str(Charles_votes)+ ")")
print('\n')     
print(f"Diana DeGette :" +str(diana_per) +" % ("+ str(Diana_votes)+ ")")
print('\n')     
print(f"Raymon Anthony Doane :" +str(raymon_per) +" % ("+ str(Raymon_votes)+ ")")
print('\n')  
print(f'----------------------------'+'\n')  
print(f"Winner :" + str(election_winner))  
print(f'----------------------------'+'\n')  

# creating a text file and adding the results to the text file
with open('Pypoll_analysis.txt', "w" ) as text:
    text.write(f'Election Results'+'\n')
    text.write(f'----------------------------'+'\n')
    text.write("Total Votes: " + str(total_vote))
    text.write(f'----------------------------'+'\n')     
    text.write(f"Charles Casper Stockham :" +str(charles_per) +" % ("+ str(Charles_votes)+ ")")
    text.write('\n')     
    text.write(f"Diana DeGette :" +str(diana_per) +" % ("+ str(Diana_votes)+ ")")
    text.write('\n')     
    text.write(f"Raymon Anthony Doane :" +str(raymon_per) +" % ("+ str(Raymon_votes)+ ")")
    text.write('\n')  
    text.write(f'----------------------------'+'\n')  
    text.write(f"Winner :" + str(election_winner))  
    text.write('\n')  
    text.write(f'----------------------------'+'\n') 
    
