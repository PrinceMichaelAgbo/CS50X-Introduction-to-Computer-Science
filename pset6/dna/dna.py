import sys
import csv

if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    sys.exit(1)

with open(sys.argv[1], "r") as csvfile:  # read the database csv file
    database_reader = csv.DictReader(csvfile, delimiter=",")
    listed1 = list(database_reader)

with open(sys.argv[1], "r") as csvfile2:  # create a list for the keys which is first line of csv file
    database_reader2 = csv.reader(csvfile2)
    database_dict = {}
    for line in database_reader2:
        keys_listed = line
        break

with open(sys.argv[2], "r") as sequences_file:  # read the sequences txt file
    sequences_reader = csv.reader(sequences_file)
    sequence_list = list(sequences_reader)
    sequence_list = sequence_list[0]


str_dict = {}
for i in keys_listed[1:]:  # to count and store number of strs in sequence file
    count = 0
    max = 0
    for j in range(0, len(sequence_list[0])):  # this accounts for multiple frames for a particular str
        if sequence_list[0][j:j+len(i)] == i:  # if found in a particular frame
            for k in range(j, len(sequence_list[0]), len(i)):
                # hold that frame constant, and count the number of repeating sequences
                if sequence_list[0][k:k+len(i)] == i:
                    count += 1
                else:
                    if (count > max):
                        max = count
                    count = 0
                    j = k  # this ensures that we continue from where we left off
                    break
    str_dict[i] = max

for j in range(len(listed1)):  # to find str matches
    flag = True
    for i in range(1, len(keys_listed)):
        if int(listed1[j][keys_listed[i]]) != int(str_dict[keys_listed[i]]):
            flag = False
            break

    if (flag):
        print(listed1[j][keys_listed[0]])
        sys.exit(0)

print("No match")

