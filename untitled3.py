import numpy as np
from matplotlib import pyplot as plt
import csv
def read_data():
    textfile = input("Choose your file: ") # gets text file name
    myfile = open(textfile) # Opens the file
    myfile_csv=csv.reader(myfile) # makes file more readible
    players = [] # List for the students
    for row in myfile_csv:
        #print(row)
        players.append(row) # Adds the list of the student into another list
    players.sort(key=lambda x: (x[0],x[1])) # Alphabetize the list by last name then firstname
    myfile.close() # Closes the file
    return players




def main():
   some_value=read_data()
   print(some_value)







if __name__=='__main__':
    main()
