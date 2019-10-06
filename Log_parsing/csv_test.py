import csv, time, glob, socket
 
# set filenames
input_file = "log.csv"
daily_output = f"fqdn_list_{time.strftime('%Y%m%d')}.txt"
master_output = "fqdn_list_master.txt"

# create list of destinations
destinations = []

# init counters
total = 0
unique = 0
master = 0

with open(input_file, "r") as log_file:
    log_reader = csv.reader(log_file)

    for row in log_reader:
        print(row)