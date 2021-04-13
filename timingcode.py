from time import time, sleep

# Sets start time
start_time = time()

# Replace sleep(75) below with code you want to time
sleep(5)

# Sets end time
end_time = time()

# Computes overall runtime in seconds
tot_time = end_time - start_time

# Prints overall runtime in seconds
print("\nTotal Elapsed Runtime:", tot_time, "in seconds.")

print(
    "\nTotal Elapsed Runtime:",
    str(int((tot_time / 3600)))
    + ":"
    + str(int(((tot_time % 3600) / 60)))
    + ":"
    + str(int(((tot_time % 3600) % 60))),
)
