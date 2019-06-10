import matplotlib.pyplot as plt
import numpy as np
import csv

outfile = open("2009result.csv", "r")
file = csv.reader(outfile)
lr = list(file)
#next(file, None)

party = []
votes = []

party.append(lr[1][3])
party.append(lr[1][8])
party.append(lr[1][13])
party.append(lr[1][18])
party.append(lr[1][23])

votes.append(lr[1][4])
votes.append(lr[1][9])
votes.append(lr[1][14])
votes.append(lr[1][19])
votes.append(lr[1][24])
print(party)
print(votes)
plt.subplot(121)
plt.pie(votes, labels=party)
plt.axis('equal') # make the pie chart circular
plt.subplot(122)
plt.pie(votes, labels=party)
plt.axis('equal') # make the pie chart circular
plt.show()

