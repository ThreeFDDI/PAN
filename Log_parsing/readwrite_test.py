master_output = "fqdn_list_master.txt"

# open existing master file
with open(master_output, "r+") as f:
    # read master file into list
    master = f.read().splitlines()
    print(master)
