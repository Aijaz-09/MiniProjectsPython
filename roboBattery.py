from operator import index

positions = [1,2,3,4,5]     # Get the positions(batteries) available in the tray or whatever as input from somewhere
badBatteries = [3, 8, 5]    # Get the positions(batteries) that are bad as input from somewhere
removed = []                # for Keeping track of the bad batteries already removed
for i in range(len(badBatteries)):
    for j in range(len(positions)):
        if badBatteries[i] == positions[j]:
            if positions[j] in removed: # If the battery is already removed
                continue                # No need to actuate(saving resources and time) and check for next Bad Battery

            else:
                removed.append(positions[j])   # Actuate to remove the battery and update removed list

print(positions)
print(badBatteries)
print(removed)


#Now again running the same logic, but the batteries are already removed, so no action(movement of robot) happens now
for i in range(len(badBatteries)):
    for j in range(len(positions)):
        if badBatteries[i] == positions[j]:
            if positions[j] in removed: # If the battery is already removed
                continue                # No need to actuate(saving resources and time) and check for next Bad Battery

            else:
                removed.append(positions[j])   # Actuate to remove the battery and update removed list

print(positions)
print(badBatteries)
print(removed)
