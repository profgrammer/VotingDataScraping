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
    party.append(row[28] + " : Rank " + row[31])
    party.append(row[33] + " : Rank " + row[36])
    party.append(row[38] + " : Rank " + row[41])
    party.append(row[43] + " : Rank " + row[46])
    party.append(row[48] + " : Rank " + row[51])
    votes.append(row[29])
    votes.append(row[34])
    votes.append(row[39])
    votes.append(row[44])
    votes.append(row[49])
    color.append(c[row[28].strip()])
    color.append(c[row[33].strip()])
    color.append(c[row[38].strip()])
    color.append(c[row[43].strip()])
    color.append(c[row[48].strip()])

    print(party)
    print(votes)
    plt.pie(votes, labels=party, autopct='%1.0f%%', colors = color)
    plt.axis('equal') # make the pie chart circular
    str1 = str(row[0]) + '_2014' + '.png'
    plt.savefig(str1, bbox_inches='tight')
    plt.close()#prevents overlapping pie charts
