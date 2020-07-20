import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



### CODE STARTS HERE: ###

# starting run time
start_time = time.time()

# names_1 list
new_names_1 = []
# open as f
with open("names_1.txt") as f:
    # read in, split on space
    new_names_1 = f.read().split("\n")

# names_2 list
new_names_2 = []
# open as f
with open("names_2.txt") as f:
    # read in, split on space
    new_names_2 = f.read().split("\n")

# duplicates
dups = []
# for names in list 1
for name in new_names_1:
    # if they are in list 2
    if name in new_names_2:
        # append them to new empty list 'dups'
        dups.append(name)

# ending run time -- printing results (code from above)
end_time = time.time()
print('New Code:')
print(f'{len(duplicates)} duplicates:\n\n{", ".join(duplicates)}\n')
print(f'New runtime: {end_time - start_time} seconds')


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
