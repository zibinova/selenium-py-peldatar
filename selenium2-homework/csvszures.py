import csv

with open("table_in.csv", "r") as file1:
    with open("table_out.csv", "w") as file2:
        reader = csv.reader(file1, delimiter=",")
        next(reader)
        for row in reader:
            res = (", ".join(row[:-2]) + "\n")
            file2.write(res)










