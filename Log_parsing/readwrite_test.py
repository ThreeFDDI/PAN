master_output = "fqdn_list_master.txt"

# open existing master file
with open(master_output, "a+") as f:
    # read master file into list
    master = f.read().splitlines()
    print(len(master))
    f.write("Add stuff to file\n")



