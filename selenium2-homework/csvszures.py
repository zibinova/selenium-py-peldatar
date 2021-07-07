import csv

with open("table_in.csv", "r") as file1:
    with open("table_out.csv", "w") as file2:
        reader = csv.reader(file1)
        line = []
        for line in file1:
            line.append
            file2.write(line)






