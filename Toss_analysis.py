import csv
import numpy as np
from matplotlib import pyplot as plt
class ipl_analysis:
    def bar_grph(self,team_names, no_of_match_toss_win,no_of_match_indiv,Tot_indiv_mat_win,Year_input):
        fig_size=plt.figure(figsize=(20, 15))
        bar_width = 0.25
        y_pos = np.arange(len(team_names)) 
        result1=plt.bar(y_pos, no_of_match_toss_win,bar_width,color='b', alpha=1, label='Toss_win_num')
        result2=plt.bar(y_pos+bar_width,no_of_match_indiv,bar_width,color='r',alpha=1, label='Total_no_num')
        result3=plt.bar(y_pos+bar_width+bar_width,Tot_indiv_mat_win,bar_width,color='g',alpha=1, label='Total_indiv_win')
        plt.ylabel('WON_NUMBERS')
        plt.xlabel('IPL_TEAM_NAMES')
        plt.title('IPL_TOSS_ANALYSIS : '+Year_input)
        plt.xticks(y_pos+bar_width, team_names)
        plt.legend()
        plt.show()

Year_input=str(input())
csv_file = open("D:\Python\ipl\matches.csv",'r')
csv_data = csv.DictReader(csv_file)
no_of_match_indiv=[]
no_of_match_toss_win=[]
Toss_parti_Teams=[]
Toss_won_team=[]
Match_won=[]
Tot_indiv_mat_win=[]
data_2014={}
for read_1 in sorted(csv_data):
    #team_names=read_1.keys()
    if read_1['season']== Year_input:
        Toss_won_team.append(read_1['toss_winner'])
        Toss_parti_Teams.append([read_1['team1'],read_1['team2']])
        Match_won.append(read_1['winner'])
Total_matches=len(Toss_won_team)
team_names=set(Toss_won_team)
for team in set(Toss_won_team):
    counter=0
    counter_win=0
    counter_mat_win=0
    for team1,team2 in Toss_parti_Teams:
        if team1==team or team2==team:
            counter+=1
    no_of_match_indiv.append(counter)
    for win_indiv in Toss_won_team:
        if win_indiv==team:
            counter_win+=1
    no_of_match_toss_win.append(counter_win)   
    for match_indiv_win in Match_won:
        if match_indiv_win== team:
            counter_mat_win+=1
    Tot_indiv_mat_win.append(counter_mat_win)
object_ipl=ipl_analysis()
object_ipl.bar_grph(team_names,no_of_match_toss_win,no_of_match_indiv,Tot_indiv_mat_win,Year_input)
