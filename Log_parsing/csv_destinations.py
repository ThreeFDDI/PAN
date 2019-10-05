import csv, socket

# open csv log file
log_file = open("log.csv")

# read csv file
log_reader = csv.reader(log_file)

# create list of destinations
destinations = []

# parse csv file destination column
for row in log_reader:
    # attempt reverse dns lookup
    fqdn = socket.getfqdn(row[8])
    
    # ignore destinations already in list
    if fqdn not in destinations:
        destinations.append(fqdn)
    
# write fqdns to file
with open("fqdn_list.txt", "a+") as f:
    for i in destinations:
        f.write(i + "\n")
