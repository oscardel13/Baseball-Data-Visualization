import numpy as np
from matplotlib import pyplot as plt
import csv
def read_data():
    textfile = input("Choose your file: ") # gets text file name
    myfile = open(textfile) # Opens the file
    myfile_csv=csv.reader(myfile) # makes file more readible
    players = [] # List for the students
    for row in myfile_csv:
        players.append(row) # Adds the list of the student into another list
    #players.sort(key=lambda x: (x[0],x[1])) # Alphabetize the list by last name then firstname
    del players[0]
    myfile.close() # Closes the file
    return players

def get_menu_choice(players):
    choice = "100"
    while (choice!="0"):
        print("0: Exit")
        print("1: Histogram of runs scored in the lifetimes of all players (no cutoff, no postions")
        print("2: Histogram of runs scored in the lifetimes of all players (no cutoff)")
        print("3: Histogram of runs scored in the lifetimes of all players (cutoff = 100)")
        print("4: Graph team presence over time")
        print("5: Find the batters that had the best and worst seasons stealing bases")
        print("6: List the 10 best seasons that batters had by on base percentage")
        print("7: Plot on base percentage for the lifetimes of players with best seasons")
        print("8: Plot homeruns over time (percentiles)")
        print("9: Plot average team RBI over time (1950 - 1959)")
        print("10: Extra Credit")
        choice = input('> ')
        if ( choice == "1"):
            pass
        if ( choice == "2"):
            pass
        if ( choice == "3"):
            pass
        if ( choice == "4"):
            pass
        if ( choice == "5"):
            pass
        if ( choice == "6"):
            pass
        if ( choice == "7"):
            pass
        if ( choice == "8"):
            pass
        if ( choice == "9"):
            pass
        if ( choice == "10"):
            pass

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

def hist( Nlist ):
    plt.xlabel('Number of total runs')
    plt.ylabel('Number of players')
    plt.title('Total runs vs number of players having that many runs')
    plt.hist(Nlist.astype(int), bins = 100, stacked = True)
    plt.show()

def main():
   playersData=np.array(read_data())
   hist(unique(playersData))
   #get_menu_choice(playersData)


if __name__=='__main__':
    main()
