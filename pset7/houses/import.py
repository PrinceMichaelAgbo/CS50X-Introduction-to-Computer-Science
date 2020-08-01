# TODO
import sys
import csv
import cs50

if len(sys.argv) != 2:
    print("Usage: python import.py data.csv")
    sys.exit(1)

db = cs50.SQL("sqlite:///students.db")

with open(sys.argv[1], "r") as students:  # opens the csv file

    # Create DictReader
    reader = csv.DictReader(students, delimiter=",")  # reads the file in as a dictionary

    for row in reader:  # for each person
        name_list = row["name"].split(" ")  # get their name as a list
        first = name_list[0]
        if len(name_list) == 2:  # some might not have middle names
            last = name_list[1]
            middle = None
        else:  # if not equal to 2, it will surely be equal to 3
            middle = name_list[1]
            last = name_list[2]
        house = row["house"]
        birth_year = row["birth"]
        db.execute("INSERT INTO students (first, middle, last, house, birth ) VALUES(?, ?, ?, ?, ?)",
                   first, middle, last, house, birth_year)
        # insert into the database as appropriate
