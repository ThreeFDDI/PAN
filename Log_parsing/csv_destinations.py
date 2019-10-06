import csv, time, socket
from os import path
 
# set filenames
input_file = "log.csv"
daily_output = f"fqdn_list_{time.strftime('%Y%m%d')}.txt"
master_output = "fqdn_list_master.txt"

# init lists for destinations
destinations = []
master = []

# init counters
total = 0

# open csv log file
with open(input_file, "r") as log_file:
    # read csv rows
    log_reader = csv.reader(log_file)
    # skip csv header
    next(log_reader)
    # parse csv rows
    for row in log_reader:
        total +=1
        # attempt reverse dns lookup
        fqdn = socket.getfqdn(row[8])
        # ignore destinations already in list
        if fqdn not in destinations:
            # add unique destinations to list
            destinations.append(fqdn)

# write fqdns to daily file 
with open(daily_output, "a+") as f:
    for i in destinations:
        f.write(i + "\n")

# if master file exists, merge destinations
if path.exists(master_output):
    pass

# create new master file if it does not exist 
else:
    with open(master_output, "w") as f:
        # copy list for count purposes
        master = destinations
        # write fqdns to master file 
        for i in destinations:
            f.write(i + "\n")

# print stuff
print(f"Total entries in current file: {total}")
print(f"Unique entries in current file: {len(destinations)}")
print(f"Total unique entries in master file: {len(master)}")

