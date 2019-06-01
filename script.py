import csv

f = open('2009.csv', 'r')

reader = csv.reader(f)

data = {}

constname = "Akkalkuwa"
count = 1
for row in reader:
    if(row[1] != constname):
        data[row[1]] = {"2009_Constituency_Number" : row[0],"2009_Constituency_Name": row[1]}
        count = 1
        constname = row[1]
    candname = "2009_Candidate_Name_" + str(count)
    candparty = "2009_Party_" + str(count)
    candvotes = "2009_Votes_" + str(count)
    pervotes = "2009_Percentage_Votes_" + str(count)
    position = "2009_Position_" + str(count)
    data[row[1]][candname] = row[2]
    data[row[1]][candparty] = row[3]
    data[row[1]][candvotes] = row[4]
    data[row[1]][pervotes] = row[6]
    data[row[1]][position] = row[5]
    count = count + 1


fw = open('2009result.csv', 'w')

d = "2009_Constituency_Number, 2009_Constituency_Name, 2009_Candidate_Name_1, 2009_Party_1, 2009_Votes_1, 2009_Percentage_Votes_1, 2009_Position_1, 2009_Candidate_Name_2, 2009_Party_2, 2009_Votes_2, 2009_Percentage_Votes_2, 2009_Position_2, 2009_Candidate_Name_3, 2009_Party_3, 2009_Votes_3, 2009_Percentage_Votes_3, 2009_Position_3, 2009_Candidate_Name_4, 2009_Party_4, 2009_Votes_4, 2009_Percentage_Votes_4, 2009_Position_4, 2009_Candidate_Name_5, 2009_Party_5, 2009_Votes_5, 2009_Percentage_Votes_5, 2009_Position_5" + "\n"
for key in data:
    d = d + data[key]["2009_Constituency_Number"] + ", " + data[key]["2009_Constituency_Name"] +", " + data[key]["2009_Candidate_Name_1"] + ", " + data[key]["2009_Party_1"] + ", " + data[key]["2009_Votes_1"] + ", " + data[key]["2009_Percentage_Votes_1"] + ", " + data[key]["2009_Position_1"] + ", " +data[key]["2009_Candidate_Name_2"] + ", " + data[key]["2009_Party_2"] + ", " + data[key]["2009_Votes_2"] + ", " + data[key]["2009_Percentage_Votes_2"] + ", " + data[key]["2009_Position_2"] + ", " +data[key]["2009_Candidate_Name_3"] + ", " + data[key]["2009_Party_3"] + ", " + data[key]["2009_Votes_3"] + ", " + data[key]["2009_Percentage_Votes_3"] + ", " + data[key]["2009_Position_3"] + ", " +data[key]["2009_Candidate_Name_4"] + ", " + data[key]["2009_Party_4"] + ", " + data[key]["2009_Votes_4"] + ", " + data[key]["2009_Percentage_Votes_4"] + ", " + data[key]["2009_Position_4"]
    if("2009_Candidate_Name_5" in data[key].keys()):
        d += ", " + data[key]["2009_Candidate_Name_5"] + ", " + data[key]["2009_Party_5"] + ", " + data[key]["2009_Votes_5"] + ", " + data[key]["2009_Percentage_Votes_5"] + ", " + data[key]["2009_Position_5"] + "\n"
    else:
        d += "\n"
fw.write(d)



    
     
