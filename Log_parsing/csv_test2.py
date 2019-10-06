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

# open csv log file
log_file = open(input_file)

# read csv file
log_reader = csv.reader(log_file)

# parse csv file destination column
for row in log_reader:
    print(row)
    