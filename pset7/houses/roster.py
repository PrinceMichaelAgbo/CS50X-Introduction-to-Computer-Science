# TODO

import sys
import csv
import cs50

if len(sys.argv) != 2:
    print("Usage: python roster.py house")
    sys.exit(1)

db = cs50.SQL("sqlite:///students.db")

list_of_dict = db.execute(
    "SELECT first, middle, last, birth FROM students WHERE students.house = ? ORDER BY last, first", (sys.argv[1],))  # returns a list of dictionaries
for row in list_of_dict:  # for each person in the list and in the specified houw
    if row['middle'] == None:  # print info as specified, some might not have middle names
        print(row['first'], row['last'] + ", born", row['birth'])
    else:
        print(row['first'], row['middle'], row['last'] + ", born", row['birth'])
