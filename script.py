import csv

f = open('2009.csv', 'r')
f1 = open('2014.csv', 'r')
f2 = open('2019.csv', 'r')
f3 = open('2009p.csv', 'r')
f4 = open('2014p.csv', 'r')

reader = csv.reader(f)
reader1= csv.reader(f1)
reader2 = csv.reader(f2)
reader3 = csv.reader(f3)
reader4 = csv.reader(f4)

lr = list(reader)
lr1 = list(reader1)
lr2 = list(reader2)
lr3 = list(reader3)
lr4 = list(reader4)

imgd = {"INC": "INC.png", "NCP": "NCP.png", "Others": "Others.png", "BJP": "BJP.png", "AIMIM": "AIMIM.png", "IND": "IND.png", "MNS": "MNS.png", "None": "Nota.png", "NOTA": "Nota.png", "SHS": "SHS.png", "SWP": "SWP.png", "VBA": "VBA.png"}

data = {}

constname = "Akkalkuwa"
count = 1

for j in range (0, len(lr)):
    
    row = lr[j]
    row1 = lr1[j]
    row2 = lr2[j]
    print(row)
    if(row[1] != constname):
        data[row[1]] = {"Constituency_Number" : row[0],"Constituency_Name": row[1]}
        count = 1
        constname = row[1]

    candname = "2009_Candidate_Name_" + str(count)
    candparty = "2009_Party_" + str(count)
    candvotes = "2009_Votes_" + str(count)
    pervotes = "2009_Percentage_Votes_" + str(count)
    position = "2009_Position_" + str(count)
    img = "2009_Image_" + str(count)
    pie = "2009_Pie"

    candname1 = "2014_Candidate_Name_" + str(count)
    candparty1 = "2014_Party_" + str(count)
    candvotes1 = "2014_Votes_" + str(count)
    pervotes1 = "2014_Percentage_Votes_" + str(count)
    position1 = "2014_Position_" + str(count)
    img1 = "2014_Image_" + str(count)
    pie1 = "2014_Pie"

    candname2 = "2019_Candidate_Name_" + str(count)
    candparty2 = "2019_Party_" + str(count)
    candvotes2 = "2019_Votes_" + str(count)
    pervotes2 = "2019_Percentage_Votes_" + str(count)
    position2 = "2019_Position_" + str(count)
    img2 = "2019_Image_" + str(count)
    pie2 = "2019_Pie"

    data[row[1]][candname] = row[2]
    data[row[1]][candparty] = row[3]
    data[row[1]][candvotes] = row[4]
    data[row[1]][pervotes] = row[6]
    data[row[1]][position] = row[5]
    data[row[1]][img] = imgd[row[3].strip()]
    data[row[1]][pie] = row[0].strip() + "_2009.png"

    data[row[1]][candname1] = row1[2]
    data[row[1]][candparty1] = row1[3]
    data[row[1]][candvotes1] = row1[4]
    data[row[1]][pervotes1] = row1[6]
    data[row[1]][position1] = row1[5]
    data[row[1]][img1] = imgd[row1[3].strip()]
    data[row[1]][pie1] = row1[0].strip() + "_2014.png"

    data[row[1]][candname2] = row2[2]
    data[row[1]][candparty2] = row2[3]
    data[row[1]][candvotes2] = row2[4]
    data[row[1]][pervotes2] = row2[6]
    data[row[1]][position2] = row2[5]
    data[row[1]][img2] = imgd[row2[3].strip()]
    data[row[1]][pie2] = row2[0].strip() + "_2019.png"


    count = count + 1


for j in range(0, len(lr3)):
    row3 = lr3[j]
    row4 = lr4[j]
    data[row3[1]]["2009_Voter_Polled"] = row3[2]
    data[row4[1]]["2014_Voter_Polled"] = row4[2]
    data[row3[1]]["2009_Total_Voters"] = row3[3]
    data[row4[1]]["2014_Total_Voters"] = row4[3]
    data[row3[1]]["2009_Voter_Turnout_Percent"] = row3[4]
    data[row4[1]]["2014_Voter_Turnout_Percent"] = row4[4]


fw = open('2009result.csv', 'w')

d = "Constituency_Number,Constituency_Name,Candidate_Name_1_2009,Party_1_2009,Votes_1_2009,Percentage_Votes_1_2009,Position_1_2009,Candidate_Name_2_2009,Party_2_2009,Votes_2_2009,Percentage_Votes_2_2009,Position_2_2009,Candidate_Name_3_2009,Party_3_2009,Votes_3_2009,Percentage_Votes_3_2009,Position_3_2009,Candidate_Name_4_2009,Party_4_2009,Votes_4_2009,Percentage_Votes_4_2009,Position_4_2009,Candidate_Name_5_2009,Party_5_2009,Votes_5_2009,Percentage_Votes_5_2009,Position_5_2009,Candidate_Name_1_2014,Party_1_2014,Votes_1_2014,Percentage_Votes_1_2014,Position_1_2014,Candidate_Name_2_2014,Party_2_2014,Votes_2_2014,Percentage_Votes_2_2014,Position_2_2014,Candidate_Name_3_2014,Party_3_2014,Votes_3_2014,Percentage_Votes_3_2014,Position_3_2014,Candidate_Name_4_2014,Party_4_2014,Votes_4_2014,Percentage_Votes_4_2014,Position_4_2014,Candidate_Name_5_2014,Party_5_2014,Votes_5_2014,Percentage_Votes_5_2014,Position_5_2014,Candidate_Name_1_2019,Party_1_2019,Votes_1_2019,Percentage_Votes_1_2019,Position_1_2019,Candidate_Name_2_2019,Party_2_2019,Votes_2_2019,Percentage_Votes_2_2019,Position_2_2019,Candidate_Name_3_2019,Party_3_2019,Votes_3_2019,Percentage_Votes_3_2019,Position_3_2019,Candidate_Name_4_2019,Party_4_2019,Votes_4_2019,Percentage_Votes_4_2019,Position_4_2019,Candidate_Name_5_2019,Party_5_2019,Votes_5_2019,Percentage_Votes_5_2019,Position_5_2019,Voter_Polled_2009,Total_Voters_2009,Voter_Turnout_Percent_2009,Voter_Polled_2014,Total_Voters_2014,Voter_Turnout_Percent_2014,@img_2009_1,@img_2009_2,@img_2009_3,@img_2009_4,@img_2009_5,@img_2014_1,@img_2014_2,@img_2014_3,@img_2014_4,@img_2014_5,@img_2019_1,@img_2019_2,@img_2019_3,@img_2019_4,@img_2019_5,@pie_2009,@pie_2014,@pie_2019"  + "\n"

for key in data:
    d = d + data[key]["Constituency_Number"] + ", " + data[key]["Constituency_Name"] +", " + data[key]["2009_Candidate_Name_1"] + ", " + data[key]["2009_Party_1"] + ", " + data[key]["2009_Votes_1"] + ", " + data[key]["2009_Percentage_Votes_1"] + ", " + data[key]["2009_Position_1"] + ", " +data[key]["2009_Candidate_Name_2"] + ", " + data[key]["2009_Party_2"] + ", " + data[key]["2009_Votes_2"] + ", " + data[key]["2009_Percentage_Votes_2"] + ", " + data[key]["2009_Position_2"] + ", " +data[key]["2009_Candidate_Name_3"] + ", " + data[key]["2009_Party_3"] + ", " + data[key]["2009_Votes_3"] + ", " + data[key]["2009_Percentage_Votes_3"] + ", " + data[key]["2009_Position_3"] + ", " +data[key]["2009_Candidate_Name_4"] + ", " + data[key]["2009_Party_4"] + ", " + data[key]["2009_Votes_4"] + ", " + data[key]["2009_Percentage_Votes_4"] + ", " + data[key]["2009_Position_4"] + ", " + data[key]["2009_Candidate_Name_5"] + ", " + data[key]["2009_Party_5"] + ", " + data[key]["2009_Votes_5"] + ", " + data[key]["2009_Percentage_Votes_5"] + ", " + data[key]["2009_Position_5"] +", " + data[key]["2014_Candidate_Name_1"] + ", " + data[key]["2014_Party_1"] + ", " + data[key]["2014_Votes_1"] + ", " + data[key]["2014_Percentage_Votes_1"] + ", " + data[key]["2014_Position_1"] + ", " +data[key]["2014_Candidate_Name_2"] + ", " + data[key]["2014_Party_2"] + ", " + data[key]["2014_Votes_2"] + ", " + data[key]["2014_Percentage_Votes_2"] + ", " + data[key]["2014_Position_2"] + ", " +data[key]["2014_Candidate_Name_3"] + ", " + data[key]["2014_Party_3"] + ", " + data[key]["2014_Votes_3"] + ", " + data[key]["2014_Percentage_Votes_3"] + ", " + data[key]["2014_Position_3"] + ", " +data[key]["2014_Candidate_Name_4"] + ", " + data[key]["2014_Party_4"] + ", " + data[key]["2014_Votes_4"] + ", " + data[key]["2014_Percentage_Votes_4"] + ", " + data[key]["2014_Position_4"] + ", " +data[key]["2014_Candidate_Name_5"] + ", " + data[key]["2014_Party_5"] + ", " + data[key]["2014_Votes_5"] + ", " + data[key]["2014_Percentage_Votes_5"] + ", " + data[key]["2014_Position_5"]  +", " + data[key]["2019_Candidate_Name_1"] + ", " + data[key]["2019_Party_1"] + ", " + data[key]["2019_Votes_1"] + ", " + data[key]["2019_Percentage_Votes_1"] + ", " + data[key]["2019_Position_1"] + ", " +data[key]["2019_Candidate_Name_2"] + ", " + data[key]["2019_Party_2"] + ", " + data[key]["2019_Votes_2"] + ", " + data[key]["2019_Percentage_Votes_2"] + ", " + data[key]["2019_Position_2"] + ", " +data[key]["2019_Candidate_Name_3"] + ", " + data[key]["2019_Party_3"] + ", " + data[key]["2019_Votes_3"] + ", " + data[key]["2019_Percentage_Votes_3"] + ", " + data[key]["2019_Position_3"] + ", " +data[key]["2019_Candidate_Name_4"] + ", " + data[key]["2019_Party_4"] + ", " + data[key]["2019_Votes_4"] + ", " + data[key]["2019_Percentage_Votes_4"] + ", " + data[key]["2019_Position_4"] + ", " +data[key]["2019_Candidate_Name_5"] + ", " + data[key]["2019_Party_5"] + ", " + data[key]["2019_Votes_5"] + ", " + data[key]["2019_Percentage_Votes_5"] + ", " + data[key]["2019_Position_5"] + ", " + data[key]["2009_Voter_Polled"] + ", "  + data[key]["2009_Total_Voters"] + ", " + data[key]["2009_Voter_Turnout_Percent"] + ", "  + data[key]["2014_Voter_Polled"] + ", " + data[key]["2014_Total_Voters"] + ", " + data[key]["2014_Voter_Turnout_Percent"]+ "," + data[key]["2009_Image_1"] + "," + data[key]["2009_Image_2"] + "," + data[key]["2009_Image_3"] + "," + data[key]["2009_Image_4"] + "," + data[key]["2009_Image_5"] + "," + data[key]["2014_Image_1"]+ "," + data[key]["2014_Image_2"] + "," +  data[key]["2014_Image_3"] + "," + data[key]["2014_Image_4"] + "," + data[key]["2014_Image_5"] + "," + data[key]["2019_Image_1"] + "," + data[key]["2019_Image_2"]+ "," +  data[key]["2019_Image_3"]+ "," + data[key]["2019_Image_4"]+ "," + data[key]["2019_Image_5"]+"," + data[key]["2009_Pie"] + "," + data[key]["2014_Pie"] +"," + data[key]["2019_Pie"] + "\n"
    
    
fw.write(d)



    
     
