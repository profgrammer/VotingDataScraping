import matplotlib.pyplot as plt
import numpy as np
import csv

outfile = open("2009result.csv", "r")
file = csv.reader(outfile)
lr = list(file)
#next(file, None)

party = []
votes = []

#plt.rcParams['font.sans-serif'] = "Montserrats"
#plt.rcParams['font.family'] = "sans-serif"

c = {"BJP" : '#F47216', "INC" : "#0B8902", "NCP" : "#154A9A", "SHS" : "#AA007A", "Others" : "#CCCCCC", "NOTA" : "#FFC00F", "IND" : "#ff0000" , "MNS" : "#681A1A", "None": "#ffe5b4", "VBA" : "#78398B"}

color = []
for j in range(1, 3):
    row = lr[j]
    party.clear()
    votes.clear()
    color.clear()
    party.append(row[53] + " : Rank " + row[56])
    party.append(row[58] + " : Rank " + row[61])
    party.append(row[63] + " : Rank " + row[66])
    party.append(row[68] + " : Rank " + row[71])
    party.append(row[73] + " : Rank " + row[76])
    votes.append(row[54])
    votes.append(row[59])
    votes.append(row[64])
    votes.append(row[69])
    votes.append(row[74])
    color.append(c[row[53].strip()])
    color.append(c[row[58].strip()])
    color.append(c[row[63].strip()])
    color.append(c[row[68].strip()])
    color.append(c[row[73].strip()])

    print(party)
    print(votes)
    plt.pie(votes, labels=party, autopct='%.0f', colors = color)
    plt.axis('equal') # make the pie chart circular
    str1 = str(row[0]) + '_2019' + '.png'
    plt.savefig(str1, bbox_inches='tight')
    plt.close()#prevents overlapping pie charts

