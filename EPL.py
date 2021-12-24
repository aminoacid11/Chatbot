import csv
file = open('epl.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)

players = []
for row in csvreader:
    players.append(row)

def player_info(pn,jn=False,sp=False,cn=False,bd=False,age=False,height=False,mv=False,citizenship=False,ntc=False,weight=False):
    player_name = pn.lower()
    for epl_row in players:
        if player_name in epl_row[0].lower():
            if jn == True:
                return epl_row[1], epl_row[0]
            elif sp == True:
                return epl_row[2], epl_row[0]
            elif cn == True:
                return epl_row[3], epl_row[0]
            elif bd == True:
                return epl_row[4], epl_row[0]
            elif age == True:
                return epl_row[5], epl_row[0]
            elif height == True:
                return epl_row[6], epl_row[0]
            elif mv == True:
                return epl_row[7], epl_row[0]
            elif citizenship == True:
                return epl_row[8], epl_row[0]
            elif ntc == True:
                return epl_row[9], epl_row[0]
            elif weight == True:
                return epl_row[10], epl_row[0]