import csv
with open("heightWeight.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
file_data.pop(0)
    
new_data = []
    
for i in range(len(file_data)) :
    number = file_data[i][1]
    new_data.append(float(number))
    
# mean formula
n = len(new_data)
total = 0

for x in new_data : 
    total += x

mean = total/n

print("this is the mean :" + str(mean))
        