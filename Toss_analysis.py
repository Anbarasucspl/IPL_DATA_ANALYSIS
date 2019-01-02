import csv
import numpy as np
from matplotlib import pyplot as plt
csv_file = open("D:\Python\ipl\matches.csv",'r')
csv_data = csv.DictReader(csv_file)
no_of_match_indiv=[]
no_of_match_toss_win=[]
Toss_parti_Teams=[]
Toss_won_team=[]
data_2014={}
for read_1 in sorted(csv_data):
    #team_names=read_1.keys()
    if read_1['season']=='2008':
        Toss_won_team.append(read_1['toss_winner'])
        Toss_parti_Teams.append([read_1['team1'],read_1['team2']])
Total_matches=len(Toss_won_team)
team_names=set(Toss_won_team)
for team in set(Toss_won_team):
    counter=0
    counter_win=0
    for team1,team2 in Toss_parti_Teams:
        if team1==team or team2==team:
            counter+=1
    no_of_match_indiv.append(counter)
    for win_indiv in Toss_won_team:
        if win_indiv==team:
            counter_win+=1
    no_of_match_toss_win.append(counter_win)          
plt.figure(figsize=(20, 10))
y_pos = np.arange(len(team_names)) 
plt.bar(y_pos, no_of_match_toss_win, align='center', alpha=1)
plt.xticks(y_pos, team_names)
plt.ylabel('TOSS_WON_NUMBERS')
plt.xlabel('IPL_TEAM_NAMES')
plt.title('IPL_TOSS_WIN_NUMBERS')
plt.show()
