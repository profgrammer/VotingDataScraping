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

c = {"BJP" : '#F47216', "INC" : "#0B8902", "NCP" : "#154A9A", "SHS" : "#FF69B4", "Others" : "#CCCCCC", "NOTA" : "#FFC00F", "IND" : "#ff0000" , "MNS" : "#681A1A", "None": "#ffe5b4", "VBA" : "#78398B", "AIMIM": "#4D4E4A", "SWP" : "#11ACB4"}

color = []
for j in range(1, len(lr)):
    row = lr[j]
    party.clear()
    votes.clear()
    color.clear()
    party.append(row[3] + " : Rank " + row[6])
    party.append(row[8] + " : Rank " + row[11])
    party.append(row[13] + " : Rank " + row[16])
    party.append(row[18] + " : Rank " + row[21])
    party.append(row[23] + " : Rank " + row[26])
    votes.append(row[4])
    votes.append(row[9])
    votes.append(row[14])
    votes.append(row[19])
    votes.append(row[24])
    color.append(c[row[3].strip()])
    color.append(c[row[8].strip()])
    color.append(c[row[13].strip()])
    color.append(c[row[18].strip()])
    color.append(c[row[23].strip()])

    print(party)
    print(votes)
    plt.pie(votes, labels=party, autopct='%1.0f%%', colors = color)
    plt.axis('equal') # make the pie chart circular
    str1 = str(row[0]) + '_2009' + '.png'
    plt.savefig(str1, bbox_inches='tight')
    plt.close()#prevents overlapping pie charts
