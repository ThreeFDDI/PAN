import csv, socket

# open csv log file
log_file = open("log.csv")

# read csv file
log_reader = csv.reader(log_file)

# create list of destinations
destinations = []

# init total count and unique count
total = 0
unique = 0
master = 0

# parse csv file destination column
for row in log_reader:
    total +=1
    # attempt reverse dns lookup
    fqdn = socket.getfqdn(row[8])
    
    # ignore destinations already in list
    if fqdn not in destinations:
        unique +=1
        destinations.append(fqdn)
    
# write fqdns to file
with open("fqdn_list.txt", "a+") as f:
    for i in destinations:
        f.write(i + "\n")

with open("fqdn_list.txt", "r") as f:
    for c, l in enumerate(f):
        pass
        master = c + 1

print(f"Total entries in current file: {total}")
print(f"Unique entries in current file: {unique}")
print(f"Total unique entries in master file: {master}")
