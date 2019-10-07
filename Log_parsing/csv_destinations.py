import os, csv, time, socket
from shutil import copyfile
from pathlib import Path

 
# set filenames
input_csv = "log.csv"
daily_output = f"fqdn_list_{time.strftime('%Y%m%d')}.txt"
master_output = "fqdn_list_master.txt"
master_backup = f"fqdn_list_backup_{time.strftime('%Y%m%d')}.txt"
master_daily = f"TES_destinations_{time.strftime('%Y%m%d')}.txt"
renamed_csv = f"log_{time.strftime('%Y%m%d')}.csv"

# init lists for destinations
destinations = []
master = []

# init counters
total = 0

# backup master file
copyfile(master_output, master_backup)

# open csv log file
with open(input_csv, "r") as log_file:
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
with open(daily_output, "w") as f:
    for i in destinations:
        f.write(i + "\n")

# check if master file exists
if os.path.exists(master_output):
    # open existing file
    with open(master_output, "r") as f:
        # read master file into list
        master = f.read().splitlines()
  
else:
    # create new master file
    Path(master_output).touch()

# open existing master file
with open(master_output, "w") as f:
    # merge master and daily destinations
    merged = set(master + destinations)
    # write fqdns to master file 
    for i in merged:
        f.write(i + "\n")

# rename log.csv 
os.rename(input_csv, renamed_csv)

# copy master list with date
copyfile(master_output, master_daily)


# print stuff
print(f"Total entries in current file: {total}")
print(f"Unique entries in current file: {len(destinations)}")
print(f"Total entries in master file before: {len(master)}")
print(f"Total entries in master file after: {len(merged)}")




