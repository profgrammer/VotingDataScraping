import csv

f = open('2009.csv', 'r')
f1 = open('2014.csv', 'r')
f2 = open('2019.csv', 'r')

reader = csv.reader(f)
reader1= csv.reader(f1)
reader2 = csv.reader(f2)

lr = list(reader)
lr1 = list(reader1)
lr2 = list(reader2)

data = {}

constname = "Akkalkuwa"
count = 1
for j in range (0, len(lr)):
    row = lr[j]
    row1 = lr1[j]
    row2 = lr2[j]
    if(row[1] != constname):
        data[row[1]] = {"Constituency_Number" : row[0],"Constituency_Name": row[1]}
        count = 1
        constname = row[1]

    candname = "2009_Candidate_Name_" + str(count)
    candparty = "2009_Party_" + str(count)
    candvotes = "2009_Votes_" + str(count)
    pervotes = "2009_Percentage_Votes_" + str(count)
    position = "2009_Position_" + str(count)

    candname1 = "2014_Candidate_Name_" + str(count)
    candparty1 = "2014_Party_" + str(count)
    candvotes1 = "2014_Votes_" + str(count)
    pervotes1 = "2014_Percentage_Votes_" + str(count)
    position1 = "2014_Position_" + str(count)

    candname2 = "2019_Candidate_Name_" + str(count)
    candparty2 = "2019_Party_" + str(count)
    candvotes2 = "2019_Votes_" + str(count)
    pervotes2 = "2019_Percentage_Votes_" + str(count)
    position2 = "2019_Position_" + str(count)
    
    data[row[1]][candname] = row[2]
    data[row[1]][candparty] = row[3]
    data[row[1]][candvotes] = row[4]
    data[row[1]][pervotes] = row[6]
    data[row[1]][position] = row[5]

    data[row[1]][candname1] = row1[2]
    data[row[1]][candparty1] = row1[3]
    data[row[1]][candvotes1] = row1[4]
    data[row[1]][pervotes1] = row1[6]
    data[row[1]][position1] = row1[5]

    data[row[1]][candname2] = row2[2]
    data[row[1]][candparty2] = row2[3]
    data[row[1]][candvotes2] = row2[4]
    data[row[1]][pervotes2] = row2[6]
    data[row[1]][position2] = row2[5]
    count = count + 1


fw = open('2009result.csv', 'w')

d = "Constituency_Number, Constituency_Name, 2009_Candidate_Name_1, 2009_Party_1, 2009_Votes_1, 2009_Percentage_Votes_1, 2009_Position_1, 2009_Candidate_Name_2, 2009_Party_2, 2009_Votes_2, 2009_Percentage_Votes_2, 2009_Position_2, 2009_Candidate_Name_3, 2009_Party_3, 2009_Votes_3, 2009_Percentage_Votes_3, 2009_Position_3, 2009_Candidate_Name_4, 2009_Party_4, 2009_Votes_4, 2009_Percentage_Votes_4, 2009_Position_4, 2009_Candidate_Name_5, 2009_Party_5, 2009_Votes_5, 2009_Percentage_Votes_5, 2009_Position_5, 2014_Candidate_Name_1, 2014_Party_1, 2014_Votes_1, 2014_Percentage_Votes_1, 2014_Position_1, 2014_Candidate_Name_2, 2014_Party_2, 2014_Votes_2, 2014_Percentage_Votes_2, 2014_Position_2, 2014_Candidate_Name_3, 2014_Party_3, 2014_Votes_3, 2014_Percentage_Votes_3, 2014_Position_3, 2014_Candidate_Name_4, 2014_Party_4, 2014_Votes_4, 2014_Percentage_Votes_4, 2014_Position_4, 2014_Candidate_Name_5, 2014_Party_5, 2014_Votes_5, 2014_Percentage_Votes_5, 2014_Position_5, 2019_Candidate_Name_1, 2019_Party_1, 2019_Votes_1, 2019_Percentage_Votes_1, 2019_Position_1, 2019_Candidate_Name_2, 2019_Party_2, 2019_Votes_2, 2019_Percentage_Votes_2, 2019_Position_2, 2019_Candidate_Name_3, 2019_Party_3, 2019_Votes_3, 2019_Percentage_Votes_3, 2019_Position_3, 2019_Candidate_Name_4, 2019_Party_4, 2019_Votes_4, 2019_Percentage_Votes_4, 2019_Position_4, 2019_Candidate_Name_5, 2019_Party_5, 2019_Votes_5, 2019_Percentage_Votes_5, 2019_Position_5"  + "\n"

for key in data:
    d = d + data[key]["Constituency_Number"] + ", " + data[key]["Constituency_Name"] +", " + data[key]["2009_Candidate_Name_1"] + ", " + data[key]["2009_Party_1"] + ", " + data[key]["2009_Votes_1"] + ", " + data[key]["2009_Percentage_Votes_1"] + ", " + data[key]["2009_Position_1"] + ", " +data[key]["2009_Candidate_Name_2"] + ", " + data[key]["2009_Party_2"] + ", " + data[key]["2009_Votes_2"] + ", " + data[key]["2009_Percentage_Votes_2"] + ", " + data[key]["2009_Position_2"] + ", " +data[key]["2009_Candidate_Name_3"] + ", " + data[key]["2009_Party_3"] + ", " + data[key]["2009_Votes_3"] + ", " + data[key]["2009_Percentage_Votes_3"] + ", " + data[key]["2009_Position_3"] + ", " +data[key]["2009_Candidate_Name_4"] + ", " + data[key]["2009_Party_4"] + ", " + data[key]["2009_Votes_4"] + ", " + data[key]["2009_Percentage_Votes_4"] + ", " + data[key]["2009_Position_4"] + ", " + data[key]["2009_Candidate_Name_5"] + ", " + data[key]["2009_Party_5"] + ", " + data[key]["2009_Votes_5"] + ", " + data[key]["2009_Percentage_Votes_5"] + ", " + data[key]["2009_Position_5"] +", " + data[key]["2014_Candidate_Name_1"] + ", " + data[key]["2014_Party_1"] + ", " + data[key]["2014_Votes_1"] + ", " + data[key]["2014_Percentage_Votes_1"] + ", " + data[key]["2014_Position_1"] + ", " +data[key]["2014_Candidate_Name_2"] + ", " + data[key]["2014_Party_2"] + ", " + data[key]["2014_Votes_2"] + ", " + data[key]["2014_Percentage_Votes_2"] + ", " + data[key]["2014_Position_2"] + ", " +data[key]["2014_Candidate_Name_3"] + ", " + data[key]["2014_Party_3"] + ", " + data[key]["2014_Votes_3"] + ", " + data[key]["2014_Percentage_Votes_3"] + ", " + data[key]["2014_Position_3"] + ", " +data[key]["2014_Candidate_Name_4"] + ", " + data[key]["2014_Party_4"] + ", " + data[key]["2014_Votes_4"] + ", " + data[key]["2014_Percentage_Votes_4"] + ", " + data[key]["2014_Position_4"] + ", " +data[key]["2014_Candidate_Name_5"] + ", " + data[key]["2014_Party_5"] + ", " + data[key]["2014_Votes_5"] + ", " + data[key]["2014_Percentage_Votes_5"] + ", " + data[key]["2014_Position_5"]  +", " + data[key]["2019_Candidate_Name_1"] + ", " + data[key]["2019_Party_1"] + ", " + data[key]["2019_Votes_1"] + ", " + data[key]["2019_Percentage_Votes_1"] + ", " + data[key]["2019_Position_1"] + ", " +data[key]["2019_Candidate_Name_2"] + ", " + data[key]["2019_Party_2"] + ", " + data[key]["2019_Votes_2"] + ", " + data[key]["2019_Percentage_Votes_2"] + ", " + data[key]["2019_Position_2"] + ", " +data[key]["2019_Candidate_Name_3"] + ", " + data[key]["2019_Party_3"] + ", " + data[key]["2019_Votes_3"] + ", " + data[key]["2019_Percentage_Votes_3"] + ", " + data[key]["2019_Position_3"] + ", " +data[key]["2019_Candidate_Name_4"] + ", " + data[key]["2019_Party_4"] + ", " + data[key]["2019_Votes_4"] + ", " + data[key]["2019_Percentage_Votes_4"] + ", " + data[key]["2019_Position_4"] + ", " +data[key]["2019_Candidate_Name_5"] + ", " + data[key]["2019_Party_5"] + ", " + data[key]["2019_Votes_5"] + ", " + data[key]["2019_Percentage_Votes_5"] + ", " + data[key]["2019_Position_5"]   + "\n"
    
   

    
fw.write(d)



    
     
