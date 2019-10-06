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
        total +=1
        # attempt reverse dns lookup
        fqdn = socket.getfqdn(row[8])
        #fqdn = row[8]
        
        # ignore destinations already in list
        if fqdn not in destinations:
            unique +=1
            destinations.append(fqdn)
        

# write fqdns to file 
with open(daily_output, "a+") as f:
    for i in destinations:
        f.write(i + "\n")

# count total entries
with open(daily_output, "r") as f:
    for c, l in enumerate(f):
        pass
        master = c + 1

read_files = glob.glob("*.txt")

with open(master_output, "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

# print stuff
print(f"Total entries in current file: {total}")
print(f"Unique entries in current file: {unique}")
print(f"Total unique entries in master file: {master}")

