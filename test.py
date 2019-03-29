import csv
list_OCG_nomi = set()
list_TCG_nomi = set()
list_onaji = set()
with open('banlist1901.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        if row[0] == 'OCG':
            list_OCG_nomi.add((row[3],row[2],row[1],row[4]))
        elif row[0] == 'TCG':
            list_TCG_nomi.add((row[3],row[2],row[1],row[4]))
for card in list_OCG_nomi:
    if card in list_TCG_nomi:
        list_onaji.add(card)
for card in list_onaji:
    list_OCG_nomi.remove(card)
    list_TCG_nomi.remove(card)
