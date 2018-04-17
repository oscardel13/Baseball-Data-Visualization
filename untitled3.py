import numpy as np
from matplotlib import pyplot as plt
import csv
class BattingData:    
    year = 0
    player_id = 1
    first_name = 2
    last_name= 3
    team_name= 4
    games = 5
    at_bats =6
    runs = 7
    hits = 8
    doubles =9
    triples =10
    home_runs=11
    rbi = 12
    walks = 13
    hbp = 14
    stolen_bases = 15 
    caught_stealing = 16 
    strike_outs = 17 
    sac_flies = 18 
    position = 19

def read_data():
    #textfile = input("Choose your file: ") # gets text file name
    myfile = open("battingData1950Present.csv") # Opens the file
    myfile_csv=csv.reader(myfile) # makes file more readible
    players = [] # List for the students
    for row in myfile_csv:
        if row[BattingData.sac_flies] == '':
            row[BattingData.sac_flies] = 0
            #print("anything")
        players.append(row)
        # Adds the list of the student into another list
    #players.sort(key=lambda x: (x[0],x[1])) # Alphabetize the list by last name then firstname
    del players[0]
    myfile.close() # Closes the file
    return players
# This function is the UI that the user can pick the program they want to run
def get_menu_choice(PlayersData):
    choice = "100"
    while (choice!="0"):
        print("0: Exit")
        print("1: Histogram of runs scored in the lifetimes of all players (no cutoff, no postions")
        print("2: Histogram of runs scored in the lifetimes of all players (no cutoff)")
        print("3: Histogram of runs scored in the lifetimes of all players (cutoff = 100)")
        print("4: Graph team presence over time")
        print("5: Find the batters that had the best and worst seasons stealing bases")
        print("6: List the 20 best seasons that batters had by on base percentage")
        print("7: Plot on base percentage for the lifetimes of players with best seasons")
        print("8: Plot homeruns over time (percentiles)")
        print("9: Plot average team RBI over time (1950 - 1959)")
        print("10: Extra Credit")
        choice = input('> ')
        if ( choice == "1"):
            uniqueHist(unique(PlayersData))
        if ( choice == "2"):
            postitionHist(UniquePostions(PlayersData,1))
        if ( choice == "3"):
            postitionHist(UniquePostions(PlayersData,2))
        if ( choice == "4"):
            scat(teamPresence(PlayersData))
        if ( choice == "5"):
            best_worst_steals(PlayersData)
        if ( choice == "6"):
           you_gonna_need_this= twenty_best_seasons(PlayersData)
        if ( choice == "7"):
            obp_for_20_best_seasons(PlayersData)
        if ( choice == "8"):
            pass
        if ( choice == "9"):
            pass
        if ( choice == "10"):
            pass
# This function makes an array of players and runs
def unique(players):
    playerID = []
    runs = []
    for row in players:
        playerID.append(row[1])
        runs.append(row[7])
    NplayerID = np.array(playerID)
    Nruns = np.array(runs)
    unique_players = np.unique(NplayerID)
    sums = []
    for group in unique_players:
        sums.append(Nruns[NplayerID == group].astype(int).sum())
    Nsums = np.array(sums)
    return Nsums
# this function plots the histogram for 3b.
def uniqueHist( Nlist ):
    plt.xlabel('Number of total runs')
    plt.ylabel('Number of players')
    plt.title('Total runs vs number of players having that many runs')
    plt.hist(Nlist.astype(int), bins = 100, stacked = True)
    plt.show()

def PositionList(list):
    playerID = []
    runs = []
    for row in list:
        playerID.append(row[0])
        runs.append(row[1])
    NplayerID = np.array(playerID)
    Nruns = np.array(runs)
    unique_players = np.unique(NplayerID)
    sums = []
    for group in unique_players:
        sums.append(Nruns[NplayerID == group].astype(int).sum())
    Nsums = np.array(sums)
    return Nsums

def PositionListCut(list): #need to edit so you can choose cutoff
    playerID = []
    runs = []
    for row in list:
        playerID.append(row[0])
        runs.append(row[1])
    NplayerID = np.array(playerID)
    Nruns = np.array(runs)
    unique_players = np.unique(NplayerID)
    sums = []
    for group in unique_players:
        if (Nruns[NplayerID == group].astype(int).sum() >=100):
            sums.append(Nruns[NplayerID == group].astype(int).sum())
    Nsums = np.array(sums)
    return Nsums

def UniquePostions(players, option):
    sums1B = []
    sums2B = []
    sums3B = []
    sumsC = []
    sumsNULL = []
    sumsOF = []
    sumsP = []
    sumsSS = []
    for row in players:
        if (row[19] == "1B"):
            sums1B.append([row[1],row[7]])
        if (row[19] == "2B"):
            sums2B.append([row[1],row[7]])
        if (row[19] == "3B"):
            sums3B.append([row[1],row[7]])
        if (row[19] == "C"):
            sumsC.append([row[1],row[7]])
        if (row[19] == "NULL"):
            sumsNULL.append([row[1],row[7]])
        if (row[19] == "OF"):
            sumsOF.append([row[1],row[7]])
        if (row[19] == "P"):
            sumsP.append([row[1],row[7]])
        if (row[19] == "SS"):
            sumsSS.append([row[1],row[7]])
    if option == 1:
        return np.array([PositionList(np.array(sums1B)),PositionList(np.array(sums2B)),PositionList(np.array(sums3B)),PositionList(np.array(sumsC)),PositionList(np.array(sumsNULL)),PositionList(np.array(sumsOF)),PositionList(np.array(sumsP)),PositionList(np.array(sumsSS))])
    if option == 2:
        return np.array([PositionListCut(np.array(sums1B)),PositionListCut(np.array(sums2B)),PositionListCut(np.array(sums3B)),PositionListCut(np.array(sumsC)),PositionListCut(np.array(sumsNULL)),PositionListCut(np.array(sumsOF)),PositionListCut(np.array(sumsP)),PositionListCut(np.array(sumsSS))])

def postitionHist(Nlist):
    plt.xlabel('Number of total runs')
    plt.ylabel('Number of players')
    plt.title('Total runs vs number of players having that many runs')
    plt.hist(Nlist, bins = 100, stacked = True, label=["1B","2B","3B","C","NULL","OF","P","SS"])
    plt.legend()
    plt.show()
    
def cutoffHist(Nlist,cut1,cut2):
    plt.xlabel('Number of total runs')
    plt.ylabel('Number of players')
    plt.title('Total runs vs number of players having that many runs')
    plt.hist(Nlist, bins = 100, stacked = True, range=(cut1,cut2),label=["1B","2B","3B","C","NULL","OF","P","SS"])
    plt.legend()
    plt.show()

def teamPresence(Nlist):
    team = []
    year = []
    for row in Nlist:
        team.append(row[4])
        year.append(row[0])  
    teamList = np.array([np.array(team),np.array(year)])
    return np.unique(teamList,axis=0)
            
def scat(Nlist):
    years = np.unique(Nlist[0])

    plt.figure(figsize=(12,12))
    
    np1 = np.asarray(Nlist[1])
    np0 = np.asarray(Nlist[0], dtype = np.int32)
    
    teams = np.unique(np1)
    height = 0
    
    for team in teams:
        indicies = np.where(np1[:] == team)
        years = np.unique(np0[indicies])
        height_array = []
        for year in years:
            height_array.append(height)
        height += 1
        plt.scatter(years, height_array, marker = "s")
    
    plt.yticks(np.arange(len(teams)), teams)   

    plt.show()
    
def twenty_best_seasons(PlayersData):
    at_bats= np.percentile(PlayersData[:, BattingData.at_bats].astype(np.int32), 25)
    games_played= np.percentile(PlayersData[:, BattingData.games].astype(np.int32), 25)
    intersections=PlayersData[np.where(np.logical_and((PlayersData[:,BattingData.at_bats].astype(np.int32)>at_bats),(PlayersData[:,BattingData.games].astype(np.int32)>games_played)))]
    hitss=(intersections[:, BattingData.hits].astype(np.int32))
    walkss=(intersections[:,BattingData.walks].astype(np.int32))
    hit_by_pitch= (intersections[:, BattingData.hbp].astype(np.int32)) 
    at_batss= (intersections[:, BattingData.at_bats].astype(np.int32))
    sacrifice_flies= (intersections[:, BattingData.sac_flies].astype(np.int32))
    final_percentage=((hitss+walkss+hit_by_pitch)/(at_batss+walkss+hit_by_pitch+sacrifice_flies))
    best_stats = np.argpartition(final_percentage, -20)[-20:]
    print(intersections[best_stats])
    
def best__and_worst_steals(player_data):
    percentile = np.percentile(player_data[:,BattingData.games].astype(int),25) 
    array_of_games = player_data[:,BattingData.games].astype(int)
    arr = player_data[np.where(array_of_games > percentile)]
    stolenbase = arr[:,BattingData.stolen_bases].astype(int)
    games = arr[:,BattingData.games].astype(int)
    caught_stealing = arr[:,BattingData.caught_stealing].astype(int)
    ratio_of_steals = (stolenbase/games)
    failed_to_steal = caught_stealing - stolenbase

   
    best_index = np.argmax(ratio_of_steals)
    print("The best base stealer is: ")
    print(arr[best_index])
    worst_index = np.argmax(failed_to_steal)
    print("The worst base stealer is: ")
    print(arr[worst_index])        
    
def obp_for_20_best_seasons(PlayersData):
    at_bats= np.percentile(PlayersData[:, BattingData.at_bats].astype(np.int32), 25)
    games_played= np.percentile(PlayersData[:, BattingData.games].astype(np.int32), 25)
    intersections=PlayersData[np.where(np.logical_and((PlayersData[:,BattingData.at_bats].astype(np.int32)>at_bats),(PlayersData[:,BattingData.games].astype(np.int32)>games_played)))]
    at_batss= (intersections[:, BattingData.at_bats].astype(np.int32))
    intersections=PlayersData[np.where(np.logical_and((PlayersData[:,BattingData.at_bats].astype(np.int32)>at_bats),(PlayersData[:,BattingData.games].astype(np.int32)>games_played)))]
    hitss=(intersections[:, BattingData.hits].astype(np.int32))
    walkss=(intersections[:,BattingData.walks].astype(np.int32))
    hit_by_pitch= (intersections[:, BattingData.hbp].astype(np.int32)) 
    at_batss= (intersections[:, BattingData.at_bats].astype(np.int32))
    sacrifice_flies= (intersections[:, BattingData.sac_flies].astype(np.int32))
    final_percentage=((hitss+walkss+hit_by_pitch)/(at_batss+walkss+hit_by_pitch+sacrifice_flies))
    best_stats = np.argpartition(final_percentage, -20)[-20:]
    total=(intersections[best_stats])
    name=np.unique(total[:,BattingData.player_id])
    last_namex= np.unique(total[:, BattingData.last_name])
    first_namex= np.unique(total[:, BattingData.first_name])
    
    final_name= []
    for i in range(10):
        final_name.append(first_namex[i]+ ","+ last_namex[i])
        
    #final_name.append(last_namex+","+first_namex)

    for i in name:
        indicies = np.where(PlayersData[:, BattingData.player_id] == i)
        temp = PlayersData[indicies]
        player_rows=PlayersData[indicies,:][0]
        unique_years_rows= np.unique(player_rows[:,BattingData.year])
        on_base_percentage= []
        years= []
        for j in np.sort(unique_years_rows):
            indicies = np.where(player_rows[:, BattingData.year].astype(np.int32) == int(j))
            rows = player_rows[indicies, :][0]
            hitssx=np.sum(rows[:, BattingData.hits].astype(np.int32))
            walkssx=np.sum(rows[:,BattingData.walks].astype(np.int32))
            hit_by_pitchx= np.sum(rows[:, BattingData.hbp].astype(np.int32)) 
            at_batssx= np.sum(rows[:, BattingData.at_bats].astype(np.int32))
            sacrifice_fliesx= np.sum(rows[:, BattingData.sac_flies].astype(np.int32))
            on_base_percentage.append((hitssx + walkssx + hit_by_pitchx)/(at_batssx + hit_by_pitchx + walkssx + sacrifice_fliesx))
            years.append(int(j))
        plt.plot(years, on_base_percentage, label= temp[0, BattingData.first_name]+" " +temp[0, BattingData.last_name])


    #plt.legend(final_name)
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.show()
    #print(final_percentage)
    #print(at_bats)
    #print(games_played)
    
    

def main():
   PlayersData=np.array(read_data(),dtype=np.str)
   get_menu_choice(PlayersData)
   
if __name__=='__main__':
    main()
