import csv

teams = {
				'Sharks':[],
				'Dragons':[],
				'Raptors':[]
				}

def divide_teams_experience():
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
	with open("roster_master.txt",'w') as roster:
		fieldnames = ['Name','Soccer Experience','Guardian Name(s)']

		roster_w = csv.DictWriter(roster, fieldnames = fieldnames)
		
		
		
		for l in range(len(teams['Sharks'])):

			teams['Sharks'][l].pop('Height (inches)')
			teams['Dragons'][l].pop('Height (inches)')
			teams['Raptors'][l].pop('Height (inches)')
			


		roster.write('\nSharks\n')
		for l in teams['Sharks']:
			roster_w.writerow(l)

		roster.write('\nDragons\n')
		for l in teams['Dragons']:
			roster_w.writerow(l)

		roster.write('\nRaptors\n')
		for l in teams['Raptors']:
			roster_w.writerow(l)















