# For this lab, you will use conditional statements to determine whether commuting is possible based on the weather, the distance to travel, and the availability of a vehicle.
#! Project 1: Travel Planner
# Helps reinforce learning for conditional statements along with logical operators
distanceMi = 5
isRaining = False
hasBike = True
hasCar = False
hasRideShareApp = True

if not distanceMi:
    print(False)
elif distanceMi <= 1:
    if not isRaining:
        print(True)
    else:
        print(False)
elif distanceMi >= 1 and distanceMi <= 6:
    if hasBike and not isRaining:
        print(True)
    else:
        print(False)
else:
    if hasCar or hasRideShareApp:
        print(True)
    else:
        print(False)