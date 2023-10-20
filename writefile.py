import csv

with open('emoji2.csv','w', newline='') as file:
    writer = csv.writer(file)
    for i in range(100):
        writer.writerow([i,'0',])
