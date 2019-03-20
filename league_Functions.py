import csv
import copy

teams = {
		'Sharks':[],
		'Dragons':[],
		'Raptors':[]
		}

def divide_teams_experience():

# This function loops through the provided .csv file. First it finds and splits evenly the experinenced 
# players between the three teams. Next it accomplishes the same task with the inexperienced players.
# the results are stored in the teams{} for future reference and use.

	with open("soccer_players.csv", 'r') as player_csv:
		fieldnames = ['Name','Height (inches)','Soccer Experience','Guardian Name(s)']
		reader = csv.DictReader(player_csv)

		n = list(reader)
		
		i = 0

		for l in n:
			if l['Soccer Experience'] == 'YES' and i < 3 :
				teams['Sharks'].append(l)
				i+=1
			elif l['Soccer Experience'] == 'YES' and i < 6 :
				teams['Dragons'].append(l)
				i+=1	
			elif l['Soccer Experience'] == 'YES' and i < 9 :
				teams['Raptors'].append(l)
				i+=1

		i = 0
		for l in n:
			if l['Soccer Experience'] == 'NO' and i < 3 :
				teams['Sharks'].append(l)
				i+=1
			elif l['Soccer Experience'] == 'NO' and i < 6 :
				teams['Dragons'].append(l)
				i+=1
			elif l['Soccer Experience'] == 'NO' and i < 9 :
				teams['Raptors'].append(l)


def build_teams():

# This function firstly creates the teams.txt output file. The first loop goes through a copy of the teams{} dictionary 
# and .pop()'s the unnecessary key fields from each teams list. The copy is used as to not modify the original global teams{}
# for future use. In loops the team name is printed first before its players are written, once the end of team list is reached
# the next loop starts for the following team.

	with open("teams.txt",'w') as roster:
		fieldnames = ['Name','Soccer Experience','Guardian Name(s)']
		roster_w = csv.DictWriter(roster, fieldnames = fieldnames)

		# .deepcopy(x,[ memo]) used here to make a copy of the dict() and all of the elements within it, 		
		teams_copy = copy.deepcopy(teams) 
		
		
		for l in range(len(teams_copy['Sharks'])):

			teams_copy['Sharks'][l].pop('Height (inches)')
			teams_copy['Dragons'][l].pop('Height (inches)')
			teams_copy['Raptors'][l].pop('Height (inches)')
			
		roster.write('\nSharks\n')
		for l in teams_copy['Sharks']:
			roster_w.writerow(l)

		roster.write('\nDragons\n')
		for l in teams_copy['Dragons']:
			roster_w.writerow(l)

		roster.write('\nRaptors\n')
		for l in teams_copy['Raptors']:
			roster_w.writerow(l)

		teams_copy.clear()













